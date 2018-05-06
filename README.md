# WHAT SESAME IS

Add, open, remove, and switch, projects or folders, using the Command Palette and Key Bindings.

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-sesame.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-sesame/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-sesame.svg?style=flat-square)](https://github.com/gerardroche/sublime-sesame/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square)](https://packagecontrol.io/packages/Sesame) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

## QUICK START

Set the location of your projects:

`Menu > Preferences > Settings`

```json
{
    "sesame.path": "~/projects"
}
```

Press `ctrl+alt+o` to open a project.

## INSTALLATION

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/packages/Sesame).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named `Sesame` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-sesame.git ~/.config/sublime-text-3/Packages/Sesame`
* OSX: `git clone https://github.com/gerardroche/sublime-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Sesame`
* Windows: `git clone https://github.com/gerardroche/sublime-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/Sesame`

## COMMANDS

Command Palette | Command | Description
--------------- | ------- | -----------
Sesame: Add | `sesame_add` | Add a project to the current window
Sesame: Open | `sesame_open` | Open a project in a new window
Sesame: Remove | `sesame_remove` | Remove a project from the current window
Sesame: Switch | `sesame_switch` | Switch to a project in the current window

## KEY BINDINGS

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

Default key bindings:

Windows / Linux | OSX | Description
--------------- | --- | -----------
`ctrl+alt+o` | `super+alt+o` | Sesame: Open

## CONFIGURATION

Key | Description | Type | Default
----|-------------|------|--------
`sesame.depth` | Number of levels deep to look for projects within projects path. | `1` or `2` | `2`
`sesame.keymaps` | Enable default key bindings. | `boolean` | `true`
`sesame.paths` | Location of your projects. | `string` | The path found in the environment variable `PROJECTS_PATH` (if it exists).
`sesame.vcs` | Include only version controlled projects e.g. Git, Mercurial, Subversion | `boolean` | `false`

### Path

`Menu > Preferences > Settings`

```json
{
    "sesame.paths": [{ 
      "path": "~/projects",
      "depth": 1
    }]
}
```

`Menu > Project > Edit Project` (per-project)

```json
{
    "settings": {
        "sesame.paths": [{ 
          "path": "~/projects",
          "depth": 1
        }]
    }
}
```

**Multiple paths**

Multiple paths can be set into a single record using a `PATH` separator (':' for POSIX or ';' for Windows) e.g.

```json
{
    "sesame.paths": [{ 
      "path": "~/projects:~/work",
      "depth": 1
      }]
}
```

**Path environment variable**

A `PROJECTS_PATH` environment variable can be used to set the default path e.g. on Linux edit `~/.profile` and add `export PROJECTS_PATH=~/projects` (may require a system restart).

### Depth

Setting `depth` to every single path in `paths` is not required. If you omit `depth`, the value fo `sesame.depth` will be applied.

The default depth is `2` which means that projects are listed using the pattern `*/*` e.g. `name/name`. If you prefer to organise your projects at a single level, set the depth to `1`.

`Menu > Preferences > Settings`

```json
{
    "sesame.depth": 1,
    "sesame.paths": [
      { 
        "path": "~/projects"
      }, 
      { 
        "path": "~/work"
      }
    ]
}
```

### Custom commands

Custom commands with alternate paths can be created:

`Menu > Preferences > Key Bindings`

```json
[
   { "keys": ["ctrl+alt+v"], "command": "sesame_open", "args": { "path": "~/vendor" } }
]
```


Add custom commands to the Command Palette:

`User/Default.sublime-commands`

```json
[
   { "caption": "Sesame: Add Vendor", "command": "sesame_add", "args": { "path": "~/vendor" } },
   { "caption": "Sesame: Open Vendor", "command": "sesame_open", "args": { "path": "~/vendor" } },
   { "caption": "Sesame: Switch Vendor", "command": "sesame_switch", "args": { "path": "~/vendor" } }
]
```

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).
