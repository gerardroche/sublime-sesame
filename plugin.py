import glob
import os
import re
import subprocess

from sublime import executable_path
from sublime import platform
from sublime import set_timeout_async
from sublime import status_message
from sublime import Window
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
                if folder[1] not in existing_folders:
                    self.folders.append(folder)

        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)
        else:
            _status_message('No projects found')

    def on_done(self, index):
        if index == -1:
            return

        if _subl_add_folder(self.window, self.folders[index][1]):
            _status_message('Added {}'.format(self.folders[index][0]))


class SesameOpenCommand(sublime_plugin.WindowCommand):

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
            _subl_open_project_in_new_window(folder_projects[0])
        elif os.path.isdir(folder):
            _subl_open_folder_in_new_window(folder)


class SesameRemoveCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.folders = self.window.folders()
        self.window.show_quick_panel(self.folders, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        self.window.run_command('remove_folder', {
            'dirs': [self.folders[index]]
        })


class SesameSwitchCommand(SesameOpenCommand):

    def on_done(self, index):
        if index == -1:
            return

        super().on_done(index)

        # TODO There's got to be a better way to switch projects
        # TODO The sidebar moves/jitters when switching projects
        self.window.run_command('close_workspace')
        self.window.run_command('close_project')
        self.window.run_command('close_all')


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

    for p in paths:
        p['path'] = os.path.expandvars(os.path.expanduser((p['path'])))
        if not os.path.isdir(p['path']):
            raise ValueError("{path} must be a valid directory".format(path=p['path']))

    defaults = {
        "depth": int(kwargs.get('depth', settings.get('sesame.depth'))),
        "vcs": bool(kwargs.get('vcs', settings.get('sesame.vcs')))
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
    globs = [_glob_path(**path) for path in paths]
    folders = _flatten_once(globs)

    return folders


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

    if vcs:
        vcs_items = []
        vcs_candidates = ('.git', '.hg', '.svn', 'CVS')
        for name, path in folders:
            for candidate in vcs_candidates:
                vcs_marker_file = os.path.join(path, candidate)
                if os.path.exists(vcs_marker_file):
                    vcs_items.append([name, path])
                    break

        folders = vcs_items

    return folders


def _subl_open_project_in_new_window(sublime_project_file):
    if not sublime_project_file:
        return

    if not re.match('^.+\\.sublime-project$', sublime_project_file):
        return

    if not os.path.isfile(sublime_project_file):
        return

    _subl_async(['--new-window', '--project', sublime_project_file])


def _subl_open_folder_in_new_window(folder):
    if not folder:
        return

    if not os.path.isdir(folder):
        return

    _subl_async(['--new-window', folder])


def _subl_add_folder(window, folder):
    if not isinstance(window, Window):
        return

    if not folder:
        return

    if not os.path.isdir(folder):
        return

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

    if folder != '.':
        folder_struct['follow_symlinks'] = True

    project_data['folders'].append(folder_struct)

    window.set_project_data(project_data)

    return True


def _subl_async(args=[]):
    set_timeout_async(lambda: _subl(args))


def _subl(args=[]):
    path = executable_path()
    if platform() == 'osx':
        app_path = path[:path.rfind('.app/') + 5]
        path = app_path + 'Contents/SharedSupport/bin/subl'

    subprocess.Popen([path] + args)
