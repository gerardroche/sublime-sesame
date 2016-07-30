# gerardroche/sublime-open-sesame

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat)](https://twitter.com/gerardroche)
[![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat)](https://github.com/gerardroche/sublime-open-sesame)
[![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat)](https://raw.githubusercontent.com/gerardroche/sublime-open-sesame/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat)](https://github.com/gerardroche/sublime-open-sesame/stargazers)

[![Sublime version](https://img.shields.io/badge/sublime-v3-lightgrey.svg?style=flat)](https://sublimetext.com)
[![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?label=release&style=flat&maxAge=2592000)](https://github.com/gerardroche/sublime-open-sesame/tags)
[![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat&maxAge=2592000)](https://packagecontrol.io/packages/open-sesame)

Open folders and projects quickly in Sublime Text

Assumes you organise your projects with the following structure:

```
. projects
├── a
│   └── name-a
├── b
│   ├── name-a
│   └── name-b
└── c
    ├── name-a
    ├── name-b
    └── name-c
```

Where the above projects names will seen as:

```
a/name-a
b/name-a
b/name-b
c/name-a
c/name-b
c/name-c
```

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

* `Open Sesame: Add Project`
* `Open Sesame: Open Project`

### Configuration

Assumes you organise your projects with the following structure:

```
. projects
├── a
│   └── name-a
├── b
│   ├── name-a
│   └── name-b
└── c
    ├── name-a
    ├── name-b
    └── name-c
```

Where the above projects names will seen as:

```
a/name-a
b/name-a
b/name-b
c/name-a
c/name-b
c/name-c
```

Projects and folders are sourced in the following order *(first one found is used)*:

**User Setting**

If an `open-sesame.projects_path` setting exists and is a valid path then it used as the default location of projects. *The tilda character (`~`) will be expanded to the user home directory.* `Preferences > Settings - User` `{ "open-sesame.projects_path": "~/projects" }`

**Environment variable**

If the environment variable `PROJECTS_PATH` exists and is a valid path then it is used as the default location of projects. *The tilda character (`~`) will be expanded to the user home directory* e.g. in Ubuntu `~/.profile` `export PROJECTS_PATH=~/projects`

#### Custom Key Binding

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
