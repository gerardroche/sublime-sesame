import os
import glob
import re
import subprocess
import sublime
import sublime_plugin

class OpenSesameCommand(sublime_plugin.WindowCommand):

    """
    Quickly open folders and projects
    """

    def run(self, path = None):
        path = projects_path(path)
        if not path:
            return

        self.quick_panel_items = quick_panel_projects_items(path)
        self.window.show_quick_panel(self.quick_panel_items[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        folder = self.quick_panel_items[0][index]
        sublime_project_files = glob.glob(folder + '/*.sublime-project')

        if len(sublime_project_files) == 1:
            open_project_in_new_window(sublime_project_files[0])
        else:
            open_folder_in_new_window(folder)

class OpenSesameAddFolderCommand(sublime_plugin.WindowCommand):

    """
    Quickly add folders
    """

    def run(self, path = None):
        path = projects_path(path)
        if not path:
            return

        self.quick_panel_items = quick_panel_projects_items(path)
        self.window.show_quick_panel(self.quick_panel_items[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        add_folder_to_current_window(self.quick_panel_items[0][index])

def projects_path(path = None):
    """
    If no path given then the path is sourced in the following order:

    1. a user setting: "open-sesame.projects_path"
    2. an environment variable: "PROJECTS_PATH"

    Returns None if path cannot be found.

    Returns False if path is not a valid directory.

    Returns the path with an initial component of ~ or ~user replaced by that
    user's home directory.
    """

    if not path:
        window = sublime.active_window()
        if window:
            view = window.active_view()
            if view:
                path = view.settings().get('open-sesame.projects_path')

    if not path:
        path = os.getenv('PROJECTS_PATH')

    if not path:
        return None

    # normalise path
    path = os.path.expanduser(path)

    if not os.path.isdir(path):
        return False

    return path

def quick_panel_projects_items(path):
    project_paths = []
    project_names = []
    for path in glob.glob(path + '/*/*/'):
        match_result = re.match('^.*\/([a-zA-Z0-9\._-]+\/[a-zA-Z0-9\._-]+)\/$', path)
        if match_result:
            project_paths.append(os.path.normpath(path))
            project_names.append(match_result.group(1))

    return (project_paths, project_names)

def open_project_in_new_window(sublime_project_file):
    """
    Open a project in a new window
    """

    if not sublime_project_file:
        return

    if not os.path.isfile(sublime_project_file):
        return

    if not re.match('^.+\.sublime-project$', sublime_project_file):
        return

    sublime.set_timeout_async(lambda: subl(['--new-window', '--project', sublime_project_file]))

def open_folder_in_new_window(folder):
    """
    Open a folder in a new window
    """

    if not folder:
        return

    if not os.path.isdir(folder):
        return

    sublime.set_timeout_async(lambda: subl(['--new-window', folder]))

def add_folder_to_current_window(folder):
    """
    Add a folder to the current window
    """

    window = sublime.active_window()
    if not window:
        return

    if not folder:
        return

    if not os.path.isdir(folder):
        return

    project_data = window.project_data() if window.project_data() else {'folders': []}

    # normalise folder
    # @todo folder should be normalised to be relative paths to project file
    folder = os.path.normpath(folder)
    project_file_name = window.project_file_name()
    if project_file_name:
        project_file_dir = os.path.dirname(project_file_name)
        if project_file_dir == folder:
            folder = '.'

    # check if it already exists
    for f in project_data['folders']:
        if f['path'] and folder == f['path']:
            return # already exists

    folder_struct = {
        'path': folder
    }

    if folder != '.':
        folder_struct['follow_symlinks'] = True

    project_data['folders'].append(folder_struct)

    window.set_project_data(project_data)

def subl(args=[]):
    # credit: randy3k/Project-Manager
    executable_path = sublime.executable_path()
    if sublime.platform() == 'osx':
        app_path = executable_path[:executable_path.rfind('.app/') + 5]
        executable_path = app_path + 'Contents/SharedSupport/bin/subl'
    subprocess.Popen([executable_path] + args)
