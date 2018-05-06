import glob
import os
import re
import subprocess

from sublime import active_window
from sublime import executable_path
from sublime import platform
from sublime import set_timeout_async
from sublime import status_message
from sublime import Window
import sublime_plugin


class SesameAddCommand(sublime_plugin.WindowCommand):

    def run(self, path=None, *args, **kwargs):
        _init()
        # Exclude folders that already exist
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

        self.folders = []
        # paths = None if path == None else [path]
        folders = _find_folders(None if path == None else [path])
        if folders:
            for folder in folders:
                if folder[1] not in existing_folders:
                    self.folders.append(folder)

        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)
        else:
            _status_message('no projects found')

    def on_done(self, index):
        if index == -1:
            return

        _subl_add_folder(self.window, self.folders[index][1])


class SesameOpenCommand(sublime_plugin.WindowCommand):

    def run(self, path=None, *args, **kwargs):
        _init()
        self.folders = _find_folders(None if path == None else [path])
        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)
        else:
            _status_message('no projects found')

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

    def run(self, *args, **kwargs):
        _init()
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
        super().on_done(index)
        if index == -1:
            return

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

def _init():
    _init_paths()
    _init_vcs()

def _init_vcs():
    vcs = _get_setting('sesame.vcs')
    if vcs:
        return

def _init_paths():
    base_paths = _get_setting('sesame.paths')
    if base_paths:
        return

    # Migrate old setting
    # DEPRECATED To be removed in v3.0.0
    base_path = _get_setting('sesame.path')
    if not base_path:
        base_path = os.getenv('PROJECTS_PATH')

    depth = int(_get_setting('sesame.depth', 2))

    base_paths = { 
        "path": base_path,
        "depth": _get_setting('sesame.depth', depth)
    }
    settings = load_settings('Preferences.sublime-settings')
    settings.set('sesame.paths', [ base_paths ])
    settings.erase('sesame.path')
    save_settings('Preferences.sublime-settings')
    _message('updated deprecated settting \'sesame.path\' to \'sesame.paths\'')

def _default_depth(base_path):
    if 'depth' in base_path:
        return base_path["depth"]

    return int(_get_setting('sesame.depth', '2'))

def _find_folders(base_paths=None):
    if not base_paths:
        base_paths = _get_setting('sesame.paths')

    if not base_paths:
        return None

    folders = []

    for base_path in base_paths:
        p = base_path["path"]
        depth = _default_depth(base_path)

        paths = p.split(os.pathsep)
        paths = [os.path.expandvars(os.path.expanduser(path)) for path in paths]

        for path in paths:
            if not os.path.isdir(path):
                raise ValueError("{path} must be a valid directory".format(path=path))

        folders.extend(_glob_paths(paths, depth))
    folders.sort()

    return folders


def _get_setting(key, default=None):
    window = active_window()
    if window:
        view = window.active_view()
        if view:
            return view.settings().get(key, default)

    return default


def _flatten_once(array_of_arrays):
    return [item for array in array_of_arrays for item in array]


def _glob_paths(paths, depth):
    globs = [_glob_path(path, depth) for path in paths]
    folders = _flatten_once(globs)

    return folders

def _glob_pattern(base_path, depth): 
    return base_path + '/' + ( '*/' * depth )

def _glob_path(base_path):
    if _get_setting('sesame.depth') == 1:
        glob_pattern = base_path + '/*/'

def _folder_match_pattern(depth):
    if depth == 1:
        if platform() == 'windows':
            return '^.*\\\\([a-zA-Z0-9 \\|\\._-]+)\\\\$'
        return '^.*\\/([a-zA-Z0-9 \\|\\._-]+)\\/$'
    
    if depth == 2:
        if platform() == 'windows':
            return '^.*\\\\([a-zA-Z0-9 \\|\\._-]+\\\\[a-zA-Z0-9  \\|\\._-]+)\\\\$'
        return '^.*\\/([a-zA-Z0-9 \\|\\._-]+\\/[a-zA-Z0-9 \\|\\._-]+)\\/$'

    raise ValueError("{depth} must be 1 or 2".format(depth=depth))

def _glob_path(base_path, depth):
    glob_pattern = _glob_pattern(base_path, depth)
    folder_match_pattern = _folder_match_pattern(depth)

    folders = []
    for folder in glob.glob(glob_pattern):
        folder_match_result = re.match(folder_match_pattern, folder)
        if folder_match_result:
            folder_name = folder_match_result.group(1)
            folder_path = os.path.normpath(folder)
            folder_struct = [folder_name, folder_path]
            if folder_struct not in folders:
                folders.append(folder_struct)

    if _get_setting('sesame.vcs'):
        vcs_items = []
        vcs_candidates = ['.git', '.hg', '.svn', 'CVS']
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
        if f['path'] and folder == f['path']:
            # already exists
            return

    folder_struct = {
        'path': folder
    }

    if folder != '.':
        folder_struct['follow_symlinks'] = True

    project_data['folders'].append(folder_struct)

    window.set_project_data(project_data)


def _subl_async(args=[]):
    set_timeout_async(lambda: _subl(args))


def _subl(args=[]):
    path = executable_path()
    if platform() == 'osx':
        app_path = path[:path.rfind('.app/') + 5]
        path = app_path + 'Contents/SharedSupport/bin/subl'

    subprocess.Popen([path] + args)
