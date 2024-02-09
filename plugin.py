# Copyright (C) 2023 Gerard Roche
#
# This file is part of Sesame.
#
# Sesame is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sesame is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sesame.  If not, see <https://www.gnu.org/licenses/>.

import glob
import os
import re
import subprocess

from sublime import Window
from sublime import executable_path
from sublime import platform
from sublime import set_timeout_async
from sublime import status_message
from sublime import version
import sublime_plugin


class SesameAddCommand(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        def existing_folders():
            existing_folders = []
            project_data = self.window.project_data()
            if project_data:
                if 'folders' in project_data:
                    for folder in project_data['folders']:
                        if folder['path']:
                            folder_path = folder['path']
                            if folder_path == '.':
                                if self.window.project_file_name():
                                    folder_path = os.path.dirname(self.window.project_file_name())

                            if folder_path not in existing_folders:
                                existing_folders.append(folder_path)

            return existing_folders

        self.folders = []
        existing_folders = existing_folders()
        folders = _find_folders(self.window, **kwargs)
        if folders:
            for folder in folders:
                # Exclude folders that already exist
                if folder[1] not in existing_folders:  # type: ignore[operator]
                    self.folders.append(folder)

        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)
        else:
            _status_message('No projects found')

    def on_done(self, index):
        if index == -1:
            return

        if _add_folder(self.window, self.folders[index][1]):
            _status_message('Added {}'.format(self.folders[index][0]))


class SesameOpenCommand(sublime_plugin.WindowCommand):

    new_window = True

    def run(self, **kwargs):
        self.folders = _find_folders(self.window, **kwargs)
        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)
        else:
            _status_message('No projects found')

    def on_done(self, index):
        if index == -1:
            return

        folder = self.folders[index][1]
        folder_projects = glob.glob(folder + '/*.sublime-project')

        if len(folder_projects) == 1 and os.path.isfile(folder_projects[0]):
            _open_project(self.window, folder_projects[0], new_window=self.new_window)
        elif os.path.isdir(folder):
            _open_folder(self.window, folder, new_window=self.new_window)

        if len(folder_projects) > 1:
            _message('expected 1 .sublime-project, found %d' % len(folder_projects))


class SesameSwitchCommand(SesameOpenCommand):

    new_window = False


class SesameRemoveCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.folders = self.window.folders()
        self.window.show_quick_panel(self.folders, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        _remove_folder(self.window, self.folders[index])


def _status_message(msg):
    status_message('Sesame: ' + msg)


def _message(msg):
    _status_message(msg)
    print('Sesame: ' + msg)


def _find_folders(window, **kwargs):
    view = window.active_view()
    if view:
        settings = view.settings()
    else:
        settings = window.settings()

    path = kwargs.get('path')
    if not path:
        path = settings.get('sesame.path')

    if not path:
        path = os.getenv('PROJECTS_PATH')

    if not path:
        return _status_message('no path found')

    if isinstance(path, str):
        paths = [{'path': p} for p in path.split(os.pathsep)]
    elif isinstance(path, list):
        paths = []
        for p in path:
            if isinstance(p, str):
                paths.append({'path': p})
            elif isinstance(p, dict):
                if 'path' in p:
                    paths.append(p)
                else:
                    raise ValueError('path is required')
            else:
                raise ValueError('path is malformed, expected str or dict, got {}'.format(type(path)))
    else:
        raise ValueError('path must be a str or list, got {}'.format(type(path)))

    for k, p in enumerate(paths):
        p['path'] = os.path.expandvars(os.path.expanduser((p['path'])))
        if not os.path.isdir(p['path']):
            del paths[k]

    if not paths:
        return []

    defaults = {
        "depth": int(kwargs.get('depth', settings.get('sesame.depth', 2))),
        "vcs": kwargs.get('vcs', settings.get('sesame.vcs'))
    }

    for p in paths:
        for k, v in defaults.items():
            if k not in p:
                p[k] = v

    folders = _glob_paths(paths)
    folders.sort()

    return folders


def _flatten_once(array_of_arrays):
    return [item for array in array_of_arrays for item in array]


def _glob_paths(paths):
    return _flatten_once([_glob_path(**path) for path in paths])


def _glob_path(path, depth, vcs):
    if depth == 1:
        glob_pattern = path + '/*/'
        if platform() == 'windows':
            folder_match_pattern = '^.*\\\\([a-zA-Z0-9 \\|\\._-]+)\\\\$'
        else:
            folder_match_pattern = '^.*\\/([a-zA-Z0-9 \\|\\._-]+)\\/$'
    else:
        glob_pattern = path + '/*/*/'
        if platform() == 'windows':
            folder_match_pattern = '^.*\\\\([a-zA-Z0-9 \\|\\._-]+\\\\[a-zA-Z0-9  \\|\\._-]+)\\\\$'
        else:
            folder_match_pattern = '^.*\\/([a-zA-Z0-9 \\|\\._-]+\\/[a-zA-Z0-9 \\|\\._-]+)\\/$'

    folders = []
    for folder in glob.glob(glob_pattern):
        folder_match_result = re.match(folder_match_pattern, folder)
        if folder_match_result:
            folder_name = folder_match_result.group(1)
            folder_path = os.path.normpath(folder)
            folder_struct = [folder_name, folder_path]
            if folder_struct not in folders:
                folders.append(folder_struct)

    if vcs is True or vcs is False:
        vcs_items = []
        vcs_candidates = ('.git', '.hg', '.svn', 'CVS')
        for name, path in folders:
            for candidate in vcs_candidates:
                vcs_marker_file = os.path.join(path, candidate)
                if os.path.exists(vcs_marker_file):
                    vcs_items.append([name, path])
                    break

        if vcs:
            return vcs_items
        else:
            return [folder for folder in folders if folder not in vcs_items]

    return folders


def _open_project(window, file: str, new_window=True) -> None:
    if not file:
        raise ValueError('argument #2 is required')

    if not re.match('^.+\\.sublime-project$', file):
        raise ValueError('argument #2 is not a valid sublime project file name')

    if not os.path.isfile(file):
        raise ValueError('argument #2 is not a valid file')

    _subl_async(window, new_window=new_window, project=file)


def _open_folder(window, folder: str, new_window=True):
    if not folder:
        raise ValueError('argument #1 is required')

    if not os.path.isdir(folder):
        raise ValueError('argument #1 is not a valid directory')

    _subl_async(window, folder, new_window=new_window)


def _add_folder(window, folder):
    if not isinstance(window, Window):
        raise ValueError('argument #1 is not a valid window')

    if not folder:
        raise ValueError('argument #2 is not a valid folder')

    if not os.path.isdir(folder):
        raise ValueError('argument #2 is not a valid directory')

    project_data = window.project_data()
    if not project_data:
        project_data = {}

    if 'folders' not in project_data:
        project_data['folders'] = []

    # Normalise folder
    # @todo folder should be normalised to be relative paths to project file
    folder = os.path.normpath(folder)
    project_file_name = window.project_file_name()
    if project_file_name:
        project_file_dir = os.path.dirname(project_file_name)
        if project_file_dir == folder:
            folder = '.'

    for f in project_data['folders']:
        if f['path'] and (folder == f['path']):
            # Already exists.
            return False

    folder_struct = {
        'path': folder
    }

    project_data['folders'].append(folder_struct)

    window.set_project_data(project_data)

    return True


def _remove_folder(window: Window, folder: str) -> None:
    window.run_command('remove_folder', {
        'dirs': [folder]
    })


def _subl_async(window, *args, new_window=None, project=None):
    cmd = []

    if new_window:
        cmd.append('--new-window')

    if project:
        cmd.append('--project')
        cmd.append(project)

    for arg in args:
        cmd.append(arg)

    if project and int(version()) >= 4053:
        window.run_command('open_project_or_workspace', {
            'file': project,
            'new_window': new_window
        })
    else:
        set_timeout_async(lambda: _subl(cmd))

        if not new_window:
            # When a new window is specified then the project or folder is opened
            # in a new window, but when a new window is not specified then the
            # the current window is replaced.
            #
            # In ST >= 4053 the command "open_project_or_workspace" is used for
            # projects, but it doesn't work for regular folders. So in earlier
            # versions and when opening and switching folders the previous
            # window needs to be closed if no new window is specified.
            window.run_command('close_workspace')
            window.run_command('close_project')
            window.run_command('close_all')


def _subl(args=[]):
    path = executable_path()
    if platform() == 'osx':
        app_path = path[:path.rfind('.app/') + 5]
        path = app_path + 'Contents/SharedSupport/bin/subl'

    subprocess.Popen([path] + list(args))
