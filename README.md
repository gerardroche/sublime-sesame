# WHAT OPEN SESAME IS

Add, open, remove, switch, and manage projects and folders, using the command palette and key bindings.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-open-sesame/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat-square)](https://packagecontrol.io/packages/open-sesame) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

![Command palette screenshot](screenshot-a.png)
![Overlay screenshot](screenshot-b.png)

## OVERVIEW

* [Installation](#installation)
* [Commands](#commands)
* [Keybindings](#key-bindings)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

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

## Commands

Command Palette | Command | Description
--------------- | ------- | -----------
Open Sesame: Add Project | `open_sesame_add_project` | Add a project to the current window
Open Sesame: Open Project | `open_sesame_open_project` | Open a project in a new window
Open Sesame: Remove Folder | `open_sesame_remove_folder` | Remove a folder from the current window
Open Sesame: Switch Project | `open_sesame_switch_project` | Add a project to the current window

## Key bindings

OS X | Windows / Linux | Description
-----|-----------------|------------
`Super+Alt+o` | `Ctrl+Alt+o` | Open Sesame: Open Project

## Configuration

Key | Description | Type | Default
----|-------------|------|--------
`open-sesame.keymaps` | Enable the default keymaps. | `boolean` | `true`
`open-sesame.projects_depth` | Number of levels deep to look for projects within projects path. | `1` or `2` | `2`
`open-sesame.projects_path` | Location of your projects. | `string` | The path found in the environment variable `PROJECTS_PATH` (if it exists).

### Projects path

`Preferences > Settings`

```json
{
    "open-sesame.projects_path": "~/projects"
}
```

`Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_path": "~/projects"
    }
}
```

#### Projects Depth

The default depth is `2` which means that projects are listed using the pattern `*/*` e.g. `your/project`.

If you prefer to organise your projects at a single level, set the depth to `1`.

`Preferences > Settings`

```json
{
    "open-sesame.projects_depth": 1
}
```

`Project > Edit Project`

```json
{
    "settings": {
        "open-sesame.projects_depth": 1
    }
}
```

#### Multiple paths

A `PATH` separator (':' for POSIX or ';' for Windows) can be used to set multiple paths e.g. `"~/projects:~/work:~/src"`.

#### PROJECTS_PATH environment variable

A `PROJECTS_PATH` environment variable can be used to set the default path e.g. on Linux edit `~/.profile` (requires system restart) with `export PROJECTS_PATH=~/projects`.

#### Custom Commands

Example of creating some custom commands for `~/vendor` path.

`Menu > Preferences > Browse Packages`

Edit `User/Default.sublime-commands` (create the file if it doesn't already exist):

```json
[
    {
        "caption": "Open Sesame: Open Vendor",
        "command": "open_sesame_open_project",
        "args": { "path": "~/vendor" }
    },
    {
        "caption": "Open Sesame: Add Vendor",
        "command": "open_sesame_add_project",
        "args": { "path": "~/vendor" }
    },
    {
        "caption": "Open Sesame: Switch Vendor",
        "command": "open_sesame_switch_project",
        "args": { "path": "~/vendor" }
    }
]
```

Add preferred key bindings:

`Menu > Preferences > Key Bindings`

```json
[
    {
        "keys": ["ctrl+alt+v"],
        "command": "open_sesame_open_project",
        "args": { "path": "~/vendor" }
    }
]
```

## CONTRIBUTING

Your issue reports and pull requests are always welcome.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
