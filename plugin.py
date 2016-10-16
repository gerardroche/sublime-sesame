import os
import glob
import re
import subprocess


import sublime
import sublime_plugin


class OpenSesameCommand(sublime_plugin.WindowCommand):

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
            open_project_in_new_window(folder_projects[0])
        elif os.path.isdir(folder):
            open_folder_in_new_window(folder)


class OpenSesameAddFolderCommand(sublime_plugin.WindowCommand):

    def run(self, path = None):
        # Exclude folders that already exist
        existing_folders = []
        project_data = self.window.project_data()
        if project_data:
            if 'folders' in project_data:
                for folder in project_data['folders']:
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

        add_folder_to_window(self.folders[index][1])


def find_folders(base_path = None):
    if not base_path:
        window = sublime.active_window()
        if window:
            view = window.active_view()
            if view:
                base_path = view.settings().get('open-sesame.projects_path')

    if not base_path:
        base_path = os.getenv('PROJECTS_PATH')

    if not base_path:
        return None

    base_path = os.path.expanduser(base_path)

    if not os.path.isdir(base_path):
        raise ValueError('base path must be a valid directory')

    folders = []

    for folder in glob.glob(base_path + '/*/*/'):
        folder_match_result = re.match('^.*\/([a-zA-Z0-9\._-]+\/[a-zA-Z0-9\._-]+)\/$', folder)
        if folder_match_result:
            folder_name = folder_match_result.group(1)
            folder_path = os.path.normpath(folder)
            folder_struct = [folder_name, folder_path]
            if folder_struct not in folders:
                folders.append(folder_struct)

    folders.sort()

    return folders


def open_project_in_new_window(sublime_project_file):
    if not sublime_project_file:
        return

    if not re.match('^.+\.sublime-project$', sublime_project_file):
        return

    if not os.path.isfile(sublime_project_file):
        return

    sublime.set_timeout_async(lambda: subl(['--new-window', '--project', sublime_project_file]))


def open_folder_in_new_window(folder):
    if not folder:
        return

    if not os.path.isdir(folder):
        return

    sublime.set_timeout_async(lambda: subl(['--new-window', folder]))


def add_folder_to_window(folder):
    if not folder:
        return

    if not os.path.isdir(folder):
        return

    window = sublime.active_window()
    if not window:
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
