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

## COMMANDS

Command | Description
------- | -----------
Open Sesame: Open Project | Open a project in a new window
Open Sesame: Add Project | Add a project to the active window

## KEY BINDINGS

OS X | Windows / Linux | Description
-----|-----------------|------------
<kbd>Super</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> | Open Sesame: Open Project

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`open-sesame.keymaps` | Enable the default keymaps. | `boolean` | `true`
`open-sesame.projects_path` | Location of projects. | `string` | `null`
`open-sesame.projects_depth` | How many levels deep projects are within projects path. | `1` or `2` | `2`

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

#### Multiple projects paths

Set multiple paths by separating them with the PATH environment separater (':' for POSIX or ';' for Windows) e.g. `"~/projects:~/work:~/src"`.

#### PROJECTS_PATH environment variable

The projects path can be configured using a PROJECTS_PATH environment variable e.g. on Linux edit `~/.profile` (requires restart) `export PROJECTS_PATH=~/projects`.

### Depth

By default projects are listed as two directory structures i.e. `projects_path/*/*`. To list projects as one directory structures i.e. `projects_path/*`, set the depth to 1.

Configure globally: `Preferences > Settings - User`

```json
{
    "open-sesame.projects_depth": 1
}
```

Per project: `Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_depth": 1
    }
}
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
