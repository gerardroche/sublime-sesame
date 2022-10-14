<h1 align="center">Sesame</h1>

<p align="center">
    <a href="https://github.com/gerardroche/sublime-sesame/tags"><img alt="Latest Version" src="https://img.shields.io/github/tag/gerardroche/sublime-sesame.svg?style=flat-square&label=version"></a>
    <a href="https://github.com/gerardroche/sublime-sesame/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/gerardroche/sublime-sesame.svg?style=flat-square"></a>
    <a href="https://packagecontrol.io/packages/Sesame"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square"></a>
</p>

## About Sesame

> "**Open sesame**" is a magical phrase in the story of "[Ali Baba and the Forty Thieves](https://en.wikipedia.org/wiki/Ali_Baba_and_the_Forty_Thieves)" in [Antoine Galland](https://en.wikipedia.org/wiki/Antoine_Galland)'s version of *[One Thousand and One Nights](https://en.wikipedia.org/wiki/Antoine_Galland)*. It opens the mouth of a cave in which forty thieves have hidden a treasure.

Sesame is a Sublime Text that provides quick opening, adding, removing, and switching of your projects.

## Installation

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/packages/Sesame).

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named **NeoVintageous** in the Sublime Text Packages directory for your platform:

**Linux**

`git clone https://github.com/gerardroche/sublime-sesame.git ~/.config/sublime-text-3/Packages/Sesame`

**OSX**

`git clone https://github.com/gerardroche/sublime-sesame.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Sesame`

**Windows**

`git clone https://github.com/gerardroche/sublime-sesame.git %APPDATA%\Sublime/ Text/ 3/Packages/Sesame`

## Quick start

Set the location of your projects.

**Menu > Preferences > Settings**

```json
{
    "sesame.path": "~/projects"
}
```

 Press `Ctrl+Alt+o` (Linux, Windows) or `Super+Alt+o` (OSX), to open a project.

## Key bindings

Configure your preferred key bindings. By default only the Open Sesame command enabled.

**Menu > Preferences > Key Bindings**

```json
[
    { "keys": ["ctrl+alt+o"], "command": "sesame_open" },
    { "keys": ["ctrl+alt+a"], "command": "sesame_add" },
    { "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
    { "keys": ["ctrl+alt+s"], "command": "sesame_switch" },
]
```

## Commands

Command Palette | Command | Description
--------------- | ------- | -----------
Sesame: Add | `sesame_add` | Add a project to the current window
Sesame: Open | `sesame_open` | Open a project in a new window
Sesame: Remove | `sesame_remove` | Remove a project from the current window
Sesame: Switch | `sesame_switch` | Switch to a project in the current window

## Configuration

Key | Description | Type | Default
----|-------------|------|--------
`sesame.path` | Location of projects. | `string` or `list[str, dict]` | The value found in the environment variable `PROJECTS_PATH` (if it exists).
`sesame.depth` | Number of levels deep to look for projects within path. | `int` `1` or `2` | `2`
`sesame.vcs` | Include/exclude version controlled projects e.g. Git, Mercurial, Subversion: `true` means include only version controlled projects, `false` means exclude them, and `null` (default), means version controlled and non-version controlled projects are included. | `boolean` or `null` | `null`
`sesame.keymaps` | Enable default key bindings. | `boolean` | `true`

### sesame.path

**Menu > Preferences > Settings**

```json
{
    "sesame.path": "~/projects"
}
```

Multiple paths can be set using a `PATH` separator (':' for POSIX or ';' for Windows):

```json
{
    "sesame.path": "~/projects:~/work:~/src"
}
```

Or as a list:

```json
{
    "sesame.path": ["~/projects", "~/work", "~/src"]
}
```

A `PROJECTS_PATH` environment variable can be used to set a default projects path (instead of using the setting `sesame.path` described above) e.g. on Linux edit `~/.profile` (may require a system restart):

```
export PROJECTS_PATH=~/projects
```

### sesame.depth

Projects are located using the pattern `*/*` e.g. `vendor/name`.

If you prefer to organise your projects on a single directory level, set the depth to `1`:

The default depth is `2`

**Menu > Preferences > Settings**

```json
{
    "sesame.depth": 2
}
```

### Multiple project paths

If you have multiple projects paths configured, you can configure the depth and other settings on a path-by-path basis in the following way. A path with no specific setting will fallback to the root setting.

**Menu > Preferences > Settings**

```json
{
    "sesame.path": [
        {"path": "~/projects/a", "depth": 1}
        {"path": "~/projects/b", "vcs": true}
    ],
    "sesame.depth": 2
}
```

### Example setups

Adding sesame commands Key Bindings.

**Menu > Preferences > Key Bindings**

```json
[
   { "keys": ["ctrl+alt+v"], "command": "sesame_open", "args": { "path": "~/vendor" } }
]
```

Adding sesame commands to the Command Palette.

**Create** `User/Default.sublime-commands`

```json
[
   { "caption": "Sesame: Open Vendor", "command": "sesame_open", "args": { "path": "~/vendor" } },
]
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).
