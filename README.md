# gerardroche/sublime-open-sesame

A plugin for Sublime Text.

Quickly open folders and projects.

**Sublime Text 3 only**

## Overview

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
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

1. Close Sublime Text.
2. Download or clone this repository to a directory named `open-sesame` in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/.config/sublime-text-3/Packages/open-sesame`
    * OS X: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/open-sesame`
    * Windows: `git clone https://github.com/gerardroche/sublime-open-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/open-sesame`
3. Restart Sublime Text to complete installation. The features listed above should now be available.

## Usage

### Command Palette

* `Open Sesame: Add Project`
* `Open Sesame: Open Project`

### Configuration

The following sources are used to find projects and folders.

**Preferences**

If a `open-sesame.projects_path` preference exists and is a valid path then it used as the default location of projects. The tilda character (`~`) will be expanded to the user home directory.

Example

`Preferences > Settings - User`

```
{
    "open-sesame.projects_path": "~/code"
}
```

**Environment variable**

If the preference above is not set then if the environment variable `PROJECTS_PATH` exists and is a valid path then it is used as the default location of projects. The tilda character (`~`) will be expanded to the user home directory.

Example on Ubuntu

`~/.profile`

```
export PROJECTS_PATH=~/code
```

#### Custom Key Binding

The following key binding is recommended.

`Preferences > Key Bindings - User`

```
{ "keys": ["ctrl+alt+p"], "command": "open_sesame" },
```

## Contributing

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).
