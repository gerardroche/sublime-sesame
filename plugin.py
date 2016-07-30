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
        self.quick_panel_items = Projects(path).quick_panel_items()
        if not self.quick_panel_items:
            return

        self.window.show_quick_panel(self.quick_panel_items[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        folder = self.quick_panel_items[0][index]
        sublime_project_files = glob.glob(folder + '/*.sublime-project')

        if len(sublime_project_files) == 1:
            Window().open_project_in_new(sublime_project_files[0])
        else:
            Window().open_folder_in_new(folder)

class OpenSesameAddFolderCommand(sublime_plugin.WindowCommand):

    """
    Quickly add folders
    """

    def run(self, path = None):

        # exclude folders already added
        exclude_paths = []
        project_data = self.window.project_data() if self.window.project_data() else {'folders': []}
        for f in project_data['folders']:
            if f['path'] and f['path'] not in exclude_paths:
                exclude_paths.append(f['path'])

        self.quick_panel_items = Projects(path).quick_panel_items(exclude_paths=exclude_paths)

        if not self.quick_panel_items:
            return

        self.window.show_quick_panel(self.quick_panel_items[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        Window().add_folder_to_current(self.quick_panel_items[0][index])

class Projects():

    def __init__(self, path = None):
        """
        If no path given then the path is sourced in the following order:
        1. "open-sesame.projects_path" setting
        2. "PROJECTS_PATH" environment variable

        Sets path with initial component of ~ or ~user replaced by that user's home directory.
        Sets path to False if path is not a valid directory.
        Sets path to None if path cannot be found.
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
            self.path = None
            return

        # normalise path
        path = os.path.expanduser(path)

        if not os.path.isdir(path):
            self.path = False

        self.path = path

    def quick_panel_items(self, exclude_paths = []):
        if not self.path:
            return None

        project_paths = []
        project_names = []
        for path in glob.glob(self.path + '/*/*/'):
            match_result = re.match('^.*\/([a-zA-Z0-9\._-]+\/[a-zA-Z0-9\._-]+)\/$', path)
            if match_result:
                project_path = os.path.normpath(path)
                project_name = match_result.group(1)

                if project_path not in exclude_paths:
                    project_paths.append(project_path)
                    project_names.append(project_name)

        return (project_paths, project_names)

class Window():

    def open_project_in_new(self, sublime_project_file):
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

    def open_folder_in_new(self, folder):
        """
        Open a folder in a new window
        """

        if not folder:
            return

        if not os.path.isdir(folder):
            return

        sublime.set_timeout_async(lambda: subl(['--new-window', folder]))

    def add_folder_to_current(self, folder):
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
