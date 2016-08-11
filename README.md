# gerardroche/sublime-open-sesame

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat)](https://twitter.com/gerardroche)
[![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat)](https://github.com/gerardroche/sublime-open-sesame)
[![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat)](https://raw.githubusercontent.com/gerardroche/sublime-open-sesame/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat)](https://github.com/gerardroche/sublime-open-sesame/stargazers)

[![Sublime version](https://img.shields.io/badge/sublime-v3-lightgrey.svg?style=flat)](https://sublimetext.com)
[![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?label=release&style=flat&maxAge=2592000)](https://github.com/gerardroche/sublime-open-sesame/tags)
[![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat&maxAge=2592000)](https://packagecontrol.io/packages/open-sesame)

Add or open folders quickly in Sublime Text.

![Screenshot](screenshot.png)

## Overview

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

## Installation

The preferred method of installation is via [Package Control](https://packagecontrol.io).

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named `open-sesame` in the Sublime Text Packages directory:
    * Linux: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/.config/sublime-text-3/Packages/open-sesame`
    * OS X: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/open-sesame`
    * Windows: `git clone https://github.com/gerardroche/sublime-open-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/open-sesame`

## Usage

Specify the location of your projects: `Preferences > Settings - User`

```
"open-sesame.projects_path": "~/projects"
```

Or set an environment variable (linux, requires system restart):

```
$ echo "export PROJECTS_PATH=~/projects" >> ~/.profile
```

Given the following location:

```
. ~/projects
├── doctrine
│   └── dbal
├── symfony
│   └── console
└── zend
    ├── mvc
    └── escaper
```

Opening a project will be prompt you with the following list to select from:

```
doctrine/dbal
symfony/console
zend/mvc
zend/escaper
```

Add a custom keybinding: `Preferences > Key Bindings - User`

```
{ "keys": ["ctrl+alt+p"], "command": "open_sesame" },
```

### Commands

* `Open Sesame: Open Project`
* `Open Sesame: Add Project Folder`

## Contributing

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).
