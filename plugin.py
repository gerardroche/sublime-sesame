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
        self.folders = find_folders(path)
        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        folder = self.folders[index][1]
        folder_projects = glob.glob(folder + '/*.sublime-project')

        if len(folder_projects) == 1 and os.path.isfile(folder_projects[0]):
            Window().open_project_in_new(folder_projects[0])
        elif os.path.isdir(folder):
            Window().open_folder_in_new(folder)

class OpenSesameAddFolderCommand(sublime_plugin.WindowCommand):

    """
    Quickly add folders
    """

    def run(self, path = None):

        # Exclude folders already added
        existing_folders = []
        if self.window.project_data():
            for folder in self.window.project_data()['folders']:
                if folder['path']:
                    if folder['path'] not in existing_folders:
                        existing_folders.append(folder['path'])

        self.folders = []
        for folder in find_folders(path):
            if folder[1] not in existing_folders:
                self.folders.append(folder)

        if self.folders:
            self.window.show_quick_panel(self.folders, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        Window().add_folder_to_current(self.folders[index][1])

def find_folders(path = None):
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
        raise ValueError('path must be a valid directory')

    projects = []

    for globbed_path in glob.glob(path + '/*/*/'):
        project = re.match('^.*\/([a-zA-Z0-9\._-]+\/[a-zA-Z0-9\._-]+)\/$', globbed_path)
        if project:
            project_name = project.group(1)
            project_path = os.path.normpath(globbed_path)
            project_struct = [project_name, project_path]
            if project_struct not in projects:
                projects.append(project_struct)

    projects.sort()

    return projects

class Window():

    def open_project_in_new(self, sublime_project_file):
        """
        Open a project in a new window
        """

        if not sublime_project_file:
            return

        if not re.match('^.+\.sublime-project$', sublime_project_file):
            return

        if not os.path.isfile(sublime_project_file):
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
