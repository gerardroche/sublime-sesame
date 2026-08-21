# Sesame

<p>
    <a href="https://packagecontrol.io/packages/Sesame"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square"></a>
</p>

Sublime Text commands to add, open, switch and remove folders and projects.

Suppose you organise your projects:

```sh
$ ~/projects
├── laravel
│   ├── framework
│   └── lumen
├── ruby
│   └── rake
```

The Sesame commands will prompt you with a fuzzy finder with selections:

```
laravel/framework
laravel/lumen
ruby/rake
```

If the folder contains a project file (`*.sublime-project`), it will be used when opening it.

## Setup

Set the projects path: `Command Palette → Preferences: Settings`

```jsonl
"sesame.path": "~/projects",
```

## Commands

| Name           | Description                  |
|----------------|------------------------------|
| Sesame: Open   | Open project or open folder. |
| Sesame: Add    | Add project or add folder.   |
| Sesame: Remove | Remove folder from window.   |
| Sesame: Switch | Switch to project or folder. |

## Bindings

| Command      | Linux / Win      | Mac               |
|--------------|------------------|-------------------|
| Sesame: Open | `Ctrl + Alt + o` | `Super + Alt + o` |

Create your preferred key bindings: `Command Palette → Preferences: Key Bindings`

Linux / Win

```jsonl
[
    { "keys": ["ctrl+alt+o"], "command": "sesame_open" },
    { "keys": ["ctrl+alt+a"], "command": "sesame_add" },
    { "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
    { "keys": ["ctrl+alt+s"], "command": "sesame_switch" }
]
```

Mac

```jsonl
[
    { "keys": ["super+alt+o"], "command": "sesame_open" },
    { "keys": ["super+alt+a"], "command": "sesame_add" },
    { "keys": ["super+alt+r"], "command": "sesame_remove" },
    { "keys": ["super+alt+s"], "command": "sesame_switch" }
]
```

## Settings

### sesame.path (required)

- Type: `string|list`

The location of projects. Environment variables and placeholders like `~` are expanded.

**Examples**

```jsonl
"sesame.path": "~/projects"
```

Set multiple paths:

```jsonl
"sesame.path": ["~/projects", "~/vendor", "~/other"]
```

Set a list of paths with specific settings for each path.

```jsonl
"sesame.path": [
    {
        "path": "~/projects",
        "depth": 1
    },
    {
        "path": "~/vendor",
        "vcs": true
    }
]
```

### sesame.depth

- Type: `integer (1 | 2)` (default = 2)

By default, Sesame looks two levels deep inside the path. This maps nicely to `vendor/name`, which is typical on services like GitHub. For example, when you organise your projects like this:

```sh
$ ~/projects
├── laravel
│   ├── framework
│   └── lumen
├── ruby
│   └── rake
```

When depth is `2`, the selections are two levels deep:

```
laravel/framework
laravel/lumen
ruby/rake
```

When depth is `1`, the selections are one level:

```
laravel
ruby
```

### sesame.keymaps

- Type: `boolean` (default `true`)

Enable default key bindings.

### sesame.vcs

- Type: `null|boolean` (default `null`)

The `sesame.vcs` setting allows you to control the inclusion of version control system projects. Here are the available options:

- `null`: This setting includes both version-controlled and non-version-controlled projects. Projects with and without vcs integration will be considered.

- `true`: With this setting, only version-controlled projects will be included. Projects without vcs integration will be excluded.

- `false`: This setting excludes version-controlled projects. Only projects without vcs integration will be considered.

## Adding custom commands

Sesame commands accept `path`, `depth`, and `vcs` arguments.

**Example**

> Packages/User/Default.sublime-commands

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
    },
]
```

There is no need to create a custom command for `Sesame: Remove` because that command prompts with the currently open projects and folders.

## Installation

Package Control installation

1. Open the Command Palette: `Ctrl+Shift+P` (Linux / Win) or `Cmd+Shift+P` (Mac).
1. Type "Package Control: Install Package" and press Enter.
1. In the input field, type "Sesame" and select it from the list of available packages.

Manual Git installation

1. Navigate to the Sublime Text Packages directory:
   Linux
   ```
   ~/.config/sublime-text/Packages
   ```
   Mac
   ```
   ~/Library/Application Support/Sublime Text/Packages
   ```
   Windows
   ```
   %APPDATA%\Sublime Text\Packages
   ```
1. Clone directly into the Packages directory:
   ```bash
   git clone https://github.com/gerardroche/sublime-sesame.git Sesame
   ```

## License

Released under the [GPL-3.0-or-later License](LICENSE).
