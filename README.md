# gerardroche/sublime-open-sesame

A plugin for Sublime Text.

Quickly open folders and projects.

**Sublime Text 3 only**

## Overview

* [Installation](#installation)
* [Usage](#usage)
* [Changelog](#changelog)
* [License](#license)

## Installation

### Package Control installation

The preferred method of installation is via Package Control.

1. Install [Package Control](https://packagecontrol.io).
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows, Linux) or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `open-sesame` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. The features listed above should now be available.

### Manual installation

1. Download or clone this repository to a directory named `open-sesame` in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/.config/sublime-text-3/Packages/open-sesame`
    * OS X: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/open-sesame`
    * Windows: `git clone https://github.com/gerardroche/sublime-open-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/open-sesame`
2. Restart Sublime Text to complete installation. The features listed above should now be available.

## Usage

The `Open Sesame: Projects` command uses the following sources to look for folders and projects to open.

**User Setting**

`Preferences > Settings - User`

```json
{
    "open-sesame.projects_path": "~/code"
}
```

**An environment variable**

On linux for example.

`~/.profile`

```
export PROJECTS_PATH=~/code
```

Now running the `Open Sesame: Projects` command will prompt to open folders and projects from `~/code/*/*`.

### Custom commands

Example

```
{
    "caption": "Open Sesame: Custom",
    "command": "open_sesame",
    "args": { "path": "~/custom-location" }
}
```

## Contributing

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).
