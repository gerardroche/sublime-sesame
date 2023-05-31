<h1 align="center">Sesame</h1>

<p align="center">
    <a href="https://packagecontrol.io/packages/Sesame"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square"></a>
</p>

![Ali Baba overhearing one of the thieves saying "Open Sesame"](open-sesame.webp)

Sesame is quick way to open, add, switch, and remove projects and folders.

The name "Sesame" is a play on the phrase "[Open Sesame](https://en.wikipedia.org/wiki/Open_sesame)". A magical phrase in the story of "[Ali Baba and the Forty Thieves](https://en.wikipedia.org/wiki/Ali_Baba_and_the_Forty_Thieves)" from Antoine Galland's version of [One Thousand and One Nights](https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights). It opens the mouth of a cave in which forty thieves have hidden a treasure.

Read [Sesame - A Sublime Text plugin](https://blog.gerardroche.com/2023/05/19/sesame-a-sublime-text-plugin/) for a quick introduction of usage.

## Installation

Install [Sesame](https://packagecontrol.io/packages/Sesame) via Package Control.

## Setup

Set the location of your projects and add your preferred key bindings.

**Menu → Preferences → Settings**

```js
"sesame.path": "~/projects",
```

**Menu → Preferences → Key Bindings**

```js
{ "keys": ["ctrl+alt+o"], "command": "sesame_open" },
{ "keys": ["ctrl+alt+a"], "command": "sesame_add" },
{ "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
{ "keys": ["ctrl+alt+s"], "command": "sesame_switch" },
```

## Commands

Command | Description
:------ | :----------
**Sesame:&nbsp;Open** | Open a project in a new window
**Sesame:&nbsp;Add** | Add a project to the current window
**Sesame:&nbsp;Remove** | Remove a project from the current window
**Sesame:&nbsp;Switch** | Switch to a project in the current window

## Settings

**Menu → Preferences → Settings**

Setting | Description | Type | Default
:------ | :---------- | :--- | :------
`sesame.path` | Location of projects. | `string` or `list[str, dict]` | The value found in the environment variable `PROJECTS_PATH` (if it exists).
`sesame.depth` | Number of levels deep to look for projects within path. | `int` `1` or `2` | `2`
`sesame.keymaps` | Enable default key bindings. | `boolean` | `true`
`sesame.vcs` | Include/exclude version controlled projects e.g. Git, Mercurial, Subversion: `true` means include only version controlled projects, `false` means exclude them, and `null` (default), means version controlled and non-version controlled projects are included. | `boolean` or `null` | `null`

### sesame.path

```js
"sesame.path": "~/projects"
```

Multiple paths can be set using a `PATH` separator (':' for POSIX or ';' for Windows):

```js
"sesame.path": "~/projects:~/work:~/src"
```

Or as a list:

```js
"sesame.path": ["~/projects", "~/work", "~/src"]
```

A `PROJECTS_PATH` environment variable can be used to set a default projects path (instead of using the setting `sesame.path` described above) e.g. on Linux edit `~/.profile` (may require a system restart):

```
export PROJECTS_PATH=~/projects
```

### sesame.depth

Projects are located using the pattern `*/*` e.g. `vendor/name`.

If you prefer to organise your projects on a single directory level, set the depth to `1`:

The default depth is `2`

```js
"sesame.depth": 2
```

### Multiple project paths

If you have multiple projects paths configured, you can configure the depth and other settings on a path-by-path basis in the following way. A path with no specific setting will fallback to the root setting.

```js
"sesame.path": [
    {"path": "~/projects/a", "depth": 1}
    {"path": "~/projects/b", "vcs": true}
],
"sesame.depth": 2
```

### Custom commands

Adding sesame commands Key Bindings.

```js
{ "keys": ["ctrl+alt+v"], "command": "sesame_open", "args": { "path": "~/vendor" } }
```

Adding sesame commands to the Command Palette. **Create** `User/Default.sublime-commands`

```js
{ "caption": "Sesame: Open Vendor", "command": "sesame_open", "args": { "path": "~/vendor" } },
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
