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

        if not path:
            view = self.window.active_view()
            if view:
                path = view.settings().get('open-sesame.projects_path')

            if not path:
                path = os.getenv('PROJECTS_PATH')

            if not path:
                return

        self.open(path)

    def open(self, path):
        if not path:
            return

        path = os.path.expanduser(path)
        if not os.path.isdir(path):
            return

        self.quick_panel_list = self.get_quick_panel_list(path)
        self.window.show_quick_panel(self.quick_panel_list[1], self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        folder = self.quick_panel_list[0][index]

        # if folder contains a .sublime-project file
        # then open the project in a new window
        # otherwise open the folder in a new window

        sublime_project_files = glob.glob(folder + '/*.sublime-project')

        if len(sublime_project_files) == 1:
            sublime_project_file = sublime_project_files[0]
        else:
            sublime_project_file = None

        if sublime_project_file:
            open_project_in_new_window(sublime_project_file)
        else:
            open_folder_in_new_window(folder)

    def get_quick_panel_list(self, path):
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

def subl(args=[]):
    # credit: randy3k/Project-Manager
    executable_path = sublime.executable_path()
    if sublime.platform() == 'osx':
        app_path = executable_path[:executable_path.rfind('.app/') + 5]
        executable_path = app_path + 'Contents/SharedSupport/bin/subl'
    subprocess.Popen([executable_path] + args)
