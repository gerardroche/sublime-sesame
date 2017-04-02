# WHAT OPEN SESAME IS

[![Minimum Sublime version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat-square)](https://packagecontrol.io/packages/open-sesame) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame/stargazers) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?label=packagecontrol&style=flat-square)](https://github.com/gerardroche/sublime-open-sesame/tags) [![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame) [![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

An alternative way to open projects in Sublime Text. Stop using the mouse to open projects when all you need is <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>o</kbd> Open Sesame.

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
<kbd>Super</kbd>+<kbd>Alt</kbd>+<kbd>o</kbd> | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>o</kbd> | Open Sesame: Open Project

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`open-sesame.keymaps` | Enable the default keymaps. | `boolean` | `true`
`open-sesame.projects_path` | Location of projects. | `string` | `null`
`open-sesame.projects_depth` | Number of levels deep to look for projects within projects path. | `1` or `2` | `2`

### Projects path

Set it globally: `Preferences > Settings - User`

```json
{
    "open-sesame.projects_path": "~/projects"
}
```

Set it per project: `Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_path": "~/projects"
    }
}
```

#### Multiple projects paths

A PATH separator (':' for POSIX or ';' for Windows) can be used to set multiple paths e.g. `"~/projects:~/work:~/src"`.

#### PROJECTS_PATH environment variable

A PROJECTS_PATH environment variable can be used to set the projects path e.g. on Linux edit `~/.profile` (requires system restart) with `export PROJECTS_PATH=~/projects`.

### Projects Depth

By default projects are listed as "2-folder" deep structures (`projects_path/*/*`) and are listed in the format `*/*` (like a `Username/Repository` part of a GitHub URL).

If you prefer to organise your projects at a single level under projects path i.e. `projects_path/*`, then set projects depth to 1.

Set it globally: `Preferences > Settings - User`

```json
{
    "open-sesame.projects_depth": 2
}
```

Set it per project: `Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_depth": 2
    }
}
```

### Custom Commands

Here is an example of custom Open Sesame commands for a specific path (in this case `~/vendor`).

`User/Default.sublime-commands`

(Find the User directory via `Menu > Preferences > Browse Packages`)

```
[
    {
        "caption": "Open Sesame: Open Vendor",
        "command": "open_sesame",
        "args": { "path": "~/vendor" }
    },
    {
        "caption": "Open Sesame: Add Vendor Folder",
        "command": "open_sesame_add_folder",
        "args": { "path": "~/vendor" }
    }
]
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
