# SESAME CHANGELOG

All notable changes are documented in this file using the [Keep a CHANGELOG](http://keepachangelog.com/) principles.

## 2.1.1 - 2024-02-09

### Fixed

- `follow_symlinks` option is commented out ST when removing folder

## [2.1.0] - 2020-01-22

* Added: Support for ST4

## [2.0.3] - 2020-01-18

* Fixed [#11](https://github.com/gerardroche/sublime-open-sesame/issues/11): Open starts working like switch

## [2.0.2] - 2020-01-13

* Fixed: ST4 fixes

## [2.0.1] - 2018-09-02

* Fixed [#10](https://github.com/gerardroche/sublime-open-sesame/issues/10): TypeError when using `CTRL+ALT+o`

## [2.0.0] - 2018-06-17

### Added

* Added [#9](https://github.com/gerardroche/sublime-open-sesame/issues/9): Skip paths that don't exist instead of raising exception
* Added [#8](https://github.com/gerardroche/sublime-sesame/pull/8): Allow overriding options for specific paths
* Added [#8](https://github.com/gerardroche/sublime-sesame/pull/8): Custom commands now accept any of the available options

### Changed

* Changed: The `sesame.vcs` setting now accepts `boolean` or *`None`*: `true` means include only version controlled projects, `false` means exclude them, and `null` (default), means include version controlled *and* non-version controlled projects.

### Removed

* Removed: Deprecated command `open_sesame`; use `sesame_open` instead
* Removed: Deprecated command `open_sesame_add_folder`; use `sesame_add` instead
* Removed: Deprecated command `open_sesame_add_project`; use `sesame_add` instead
* Removed: Deprecated command `open_sesame_open_project`; use `sesame_open` instead
* Removed: Deprecated command `open_sesame_remove_folder`; use `sesame_remove` instead
* Removed: Deprecated command `open_sesame_switch_project`; use `sesame_switch` instead

## [1.8.0] - 2017-11-29

Important! The plugin has been renamed "Sesame" (the old name was open-sesame).

What you need to do:

* Update your key bindings (if you created any).
* Update your custom commands (if you've created any).
* Rename the plugin folder to "Sesame" (if you installed manually).
* Update the Git repository URL to https://github.com/gerardroche/sublime-sesame.git (if you installed manually via Git).

Old settings `open-sesame.*` have been renamed `sesame.*`, these will be auto migrated so there is nothing for you to do.

### Changed

* Changed: Renamed plugin name from "open-sesame" to "Sesame"

### Deprecated

* Deprecated: `open_sesame_add_folder` command; use `sesame_add` instead
* Deprecated: `open_sesame_add_project` command; use `sesame_add` instead
* Deprecated: `open_sesame_open_project` command; use `sesame_open` instead
* Deprecated: `open_sesame_remove_folder` command; use `sesame_remove` instead
* Deprecated: `open_sesame_switch_project` command; use `sesame_switch` instead
* Deprecated: `open_sesame` command; use `sesame_open` instead
* Deprecated: `open-sesame.*` settings; use `sesame.*` instead; existing settings are auto migrated to the new settings so there is nothing for you to do.

## [1.7.0] - 2017-09-15

### Added

* Added [#7](https://github.com/gerardroche/sublime-open-sesame/issues/7): Option to only include version controlled projects e.g. Git, Mercurial, Subversion

## [1.6.0] - 2017-08-27

### Added

* Added: Switch Project command
* Added: Remove Folder command
* Added: Documentation setup guide
* Added: Documentation setup key bindings

### Deprecated

* Deprecated: `projects_path` and `projects_depth` settings; renamed to `path` and `depth` respectively; existing settings are auto migrated to the new settings so there is nothing for you to do.
* Deprecated: `open_sesame` command; use `open_sesame_open_project` instead
* Deprecated: `open_sesame_add_folder` command; use `open_sesame_add_project` instead

## [1.5.7] - 2017-08-26

### Fixed

* Fixed: Projects depth setting (regression)

## [1.5.6] - 2017-08-26

### Fixed

* Fixed: Custom commands don't work
* Fixed: Edge case exception raised when no projects found

## [1.5.5] - 2017-06-03

### Fixed

* Fixed: AttributeError: 'Window' object has no attribute 'active_project_file_name'

## [1.5.4] - 2017-06-03

### Fixed

* Fixed: Add Project Folder command select list shouldn't included current project

## [1.5.3] - 2017-04-22

### Fixed

* Fixed: should display a status message if no projects are found

## [1.5.2] - 2017-04-19

### Fixed

* Fixed [#6](https://github.com/gerardroche/sublime-open-sesame/issues/6): Cannot open folders that a pipe character in the name
* Fixed: Cannot open folders that have a space in the name

## [1.5.1] - 2017-04-14

### Fixed

* Fixed: 'projects_path' setting now expands environment variables

## [1.5.0] - 2017-04-02

### Added

* Added: `o` mnemonic for `Project → open Sesame` menu

### Changed

* Changed: `Project → open Sesame` menu now opens Command Palette with a list of all available commands

### Fixed

* Fixed: Project names containing spaces are now included in project list

## [1.4.0] - 2017-03-29

### Added

* Added [#4](https://github.com/gerardroche/sublime-open-sesame/issues/4): Single level directory projects structures

## [1.3.1] - 2017-03-24

### Fixed

* Fixed: Projects path (Windows)
* Fixed: Preferences menus

## [1.3.0] - 2017-02-09

### Added

* Added [#3](https://github.com/gerardroche/sublime-open-sesame/pull/3): Allow for multiple project (@tijn)

## [1.2.2] - 2016-12-14

### Fixed

* Fixed: adding folder doesn't work

## [1.2.1] - 2016-10-28

### Fixed

* Fixed: Race condition when adding a folder to the active window

## [1.2.0] - 2016-10-16

### Added

* Added: Open Sesame Project Menu
* Added: Default keymap <kbd>Ctrl+Shift+O</kbd> (Win, Linux) <kbd>Super+Shift+O</kbd> (OSX)

## [1.1.1] - 2016-10-01

### Fixed

* Fixed: error trying to add a folder when the project has no existing folders

## [1.1.0] - 2016-08-11

### Added

* Added: project path is now displayed below project name in quick panel list

## [1.0.0] - 2016-08-01

### Added

* Added: readme usage and badges via shields.io

## [0.5.0] - 2016-06-22

### Changed

* Changed: "Open Sesame: Add Folder" caption to "Open Sesame: Add Project Folder"

## [0.4.0] - 2016-05-11

### Changed

* Changed: "Open Sesame: Add Project" command caption to "Open Sesame: Add Folder"

### Fixed

* Fixed: The Add Folder command now only displays folders that have not already been added

## [0.3.0] - 2015-11-17

### Added

* Added: "Open Sesame: Add Folder" command

### Changed

* Changed: "Open Sesame: Project" command caption to "Open Sesame: Open Project"

## [0.2.1] - 2015-11-13

### Fixed

* Fixed: #1 should only prompts to open projects and folders not files
* Fixed: #2 should not raise runtime error if any projects folder contains special characters

## [0.2.0] - 2015-11-03

### Added

* Added: CHANGELOG link to package settings menu

## 0.1.0 - 2015-10-29

* Initial import

[2.0.4]: https://github.com/gerardroche/sublime-open-sesame/compare/2.0.3...2.0.4
[2.0.3]: https://github.com/gerardroche/sublime-open-sesame/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/gerardroche/sublime-open-sesame/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/gerardroche/sublime-open-sesame/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.8.0...2.0.0
[1.8.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.7.0...1.8.0
[1.7.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.6.0...1.7.0
[1.6.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.7...1.6.0
[1.5.7]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.6...1.5.7
[1.5.6]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.5...1.5.6
[1.5.5]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.4...1.5.5
[1.5.4]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.3...1.5.4
[1.5.3]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.2...1.5.3
[1.5.2]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.1...1.5.2
[1.5.1]: https://github.com/gerardroche/sublime-open-sesame/compare/1.5.0...1.5.1
[1.5.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.4.0...1.5.0
[1.4.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.3.1...1.4.0
[1.3.1]: https://github.com/gerardroche/sublime-open-sesame/compare/1.3.0...1.3.1
[1.3.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.2.2...1.3.0
[1.2.2]: https://github.com/gerardroche/sublime-open-sesame/compare/1.2.1...1.2.2
[1.2.1]: https://github.com/gerardroche/sublime-open-sesame/compare/1.2.0...1.2.1
[1.2.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.1.1...1.2.0
[1.1.1]: https://github.com/gerardroche/sublime-open-sesame/compare/1.1.0...1.1.1
[1.1.0]: https://github.com/gerardroche/sublime-open-sesame/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/gerardroche/sublime-open-sesame/compare/0.5.0...1.0.0
[0.5.0]: https://github.com/gerardroche/sublime-open-sesame/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/gerardroche/sublime-open-sesame/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/gerardroche/sublime-open-sesame/compare/0.2.0...0.3.0
[0.2.1]: https://github.com/gerardroche/sublime-open-sesame/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/gerardroche/sublime-open-sesame/compare/0.1.0...0.2.0
