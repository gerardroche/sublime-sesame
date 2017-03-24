# WHAT OPEN SESAME IS

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche) [![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame) [![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat-square)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame/stargazers) [![Sublime version](https://img.shields.io/badge/sublime-v3.0.0-green.svg?style=flat-square)](https://sublimetext.com) [![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?label=release&style=flat-square&maxAge=2592000)](https://github.com/gerardroche/sublime-open-sesame/tags) [![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat-square&maxAge=2592000)](https://packagecontrol.io/packages/open-sesame)

Add, open and launch folders and projects quickly in Sublime Text.

![Screenshot](screenshot.png)

## OVERVIEW

* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Installation](#installation)
* [Changelog](#changelog)
* [License](#license)

Configure the location of projects: `Preferences > Settings - User`

```json
{
    "open-sesame.projects_path": "~/projects"
}
```

```
. ~/projects
├── doctrine
│   └── dbal
├── symfony
│   └── console
└── zend
    └── escaper
```

Invoking Open Sesame given the above folder configuration and folder structure (<kbd>Ctrl+Alt+O</kbd> or <kbd>Super+Alt+O</kbd> on OSX) opens a quick panel list of projects to open in the format `vendor/name`:

```
doctrine/dbal
symfony/console
zend/escaper
```

## COMMANDS

Command | Description
------- | -----------
Open Sesame: Open Project | Open a project in a new window
Open Sesame: Add Project Folder | Add a project to the active window

## KEY BINDINGS

OS X | Windows / Linux | Description
-----|-----------------|------------
<kbd>Super</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> | Open Sesame: Open Project

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`open-sesame.keymaps` | Disable the default keymaps. | `boolean` | `true`
`open-sesame.projects_path` | Path(s) to search for projects. | `string` | `null`

### Projects path

The projects path can be configured globally: `Preferences > Settings - User`

```json
{
    "open-sesame.projects_path": "~/projects"
}
```

The projects path can also be configured per project: `Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_path": "~/projects"
    }
}
```

Multiple projects paths can be configured by using a path separater (':' for POSIX or ';' for Windows): `Preferences > Settings - User`

```json
{
    "open-sesame.projects_path": "~/work:~/src"
}
```

Alternatively, an environment variable (`PROJECTS_PATH`) can be used to specify the projects path. For example, on Linux set a projects path environment in `~/.profile` (requires restart):

```sh
echo "export PROJECTS_PATH=~/projects" >> ~/.profile
```

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named `open-sesame` in the Sublime Text Packages directory:
    * Linux: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/.config/sublime-text-3/Packages/open-sesame`
    * OS X: `git clone https://github.com/gerardroche/sublime-open-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/open-sesame`
    * Windows: `git clone https://github.com/gerardroche/sublime-open-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/open-sesame`
3. Done!

## CONTRIBUTING

Your issue reports and pull requests are always welcome.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
