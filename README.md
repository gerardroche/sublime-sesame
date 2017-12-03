# WHAT SESAME IS

Add, open, remove, switch, projects and folders, using the command palette and key bindings.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-open-sesame.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-open-sesame/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-open-sesame.svg?style=flat-square)](https://github.com/gerardroche/sublime-open-sesame/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/open-sesame.svg?style=flat-square)](https://packagecontrol.io/packages/open-sesame) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

Set the location of your projects:

`Preferences > Settings`

```json
{
    "sesame.path": "~/projects"
}
```

![Command palette screenshot](screenshot-a.png)

Adding, opening, or switching a project will prompt an overlay for you to select a project.

Projects are listed in the format `x/y` by default:

![Overlay screenshot](screenshot-b.png)

If you prefer to organise your projects at a single level then set depth to `1`:

`Preferences > Settings`

```json
{
    "sesame.depth": 1
}
```

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named `Sesame` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-sesame.git ~/.config/sublime-text-3/Packages/Sesame`
* OSX: `git clone https://github.com/gerardroche/sublime-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Sesame`
* Windows: `git clone https://github.com/gerardroche/sublime-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/Sesame`

## COMMANDS

Command Palette | Command | Description
--------------- | ------- | -----------
Sesame: Add Project | `sesame_add` | Add a project to the current window
Sesame: Open Project | `sesame_open` | Open a project in a new window
Sesame: Remove Folder | `sesame_remove` | Remove a folder from the current window
Sesame: Switch Project | `sesame_switch` | Add a project to the current window

## KEY BINDINGS

Windows / Linux | OSX | Description
--------------- | --- | -----------
`Ctrl+Alt+O` | `Super+Alt+O` | Sesame: Open Project

Add your preferred key bindings:

`Menu > Preferences > Key Bindings`

```json
[
    { "keys": ["ctrl+alt+a"], "command": "sesame_add" },
    { "keys": ["ctrl+alt+o"], "command": "sesame_open" },
    { "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
    { "keys": ["ctrl+alt+s"], "command": "sesame_switch" },
]
```

On Ubuntu you may have conflict issues with key bindings such as `ctrl+alt+s` that may be mapped to something like the system `toggle-shaded` window command. You can clear the system keybinding with a command at terminal. If you have issues with key bindings on Ubuntu, ping me on twitter and I'll do my best to help you resolve it.

    $ gsettings set org.gnome.desktop.wm.keybindings toggle-shaded "[]"

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`sesame.depth` | Number of levels deep to look for projects within projects path. | `1` or `2` | `2`
`sesame.keymaps` | Enable the default keymaps. | `boolean` | `true`
`sesame.path` | Location of your projects. | `string` | The path found in the environment variable `PROJECTS_PATH` (if it exists).
`sesame.vcs` | Include only version controlled projects e.g. Git, Mercurial, Subversion | `boolean` | `false`

### Path

`Preferences > Settings`

```json
{
    "sesame.path": "~/projects"
}
```

`Project > Edit Project`

```json
{
    "settings": {
        "sesame.path": "~/projects"
    }
}
```

#### Depth

The default depth is `2` which means that projects are listed using the pattern `*/*` e.g. `your/project`.

If you prefer to organise your projects at a single level, set the depth to `1`.

`Preferences > Settings`

```json
{
    "sesame.depth": 1
}
```

`Project > Edit Project`

```json
{
    "settings": {
        "sesame.depth": 1
    }
}
```

#### Multiple paths

Multiple paths can be set using a `PATH` separator (':' for POSIX or ';' for Windows) e.g. `"~/projects:~/work:~/src"`.

#### PROJECTS_PATH environment variable

A `PROJECTS_PATH` environment variable can be used to set the default path e.g. on Linux edit `~/.profile` (requires system restart) with `export PROJECTS_PATH=~/projects`.

#### Additional custom commands

Example of creating some custom commands for `~/vendor` path.

`Menu > Preferences > Browse Packages`

Edit `User/Default.sublime-commands` (create the file if it doesn't already exist):

```json
[
    {
        "caption": "Sesame: Add Vendor",
        "command": "sesame_add",
        "args": { "path": "~/vendor" }
    },
    {
        "caption": "Sesame: Open Vendor",
        "command": "sesame_open",
        "args": { "path": "~/vendor" }
    },
    {
        "caption": "Sesame: Switch Vendor",
        "command": "sesame_switch",
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
        "command": "sesame_open",
        "args": { "path": "~/vendor" }
    }
]
```

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
