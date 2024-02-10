# Sesame - A command palette for projects

Sesame is a command palette for projects. It provides commands to open, add, switch, and remove your projects.

<p>
    <a href="https://packagecontrol.io/packages/Sesame"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square"></a>
</p>

## Installation

**Package Control installation**

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette.
1. Type "Package Control: Install Package" and press Enter.
1. In the input field, type "Sesame" and select it from the list of available packages.

**Manual Git installation**

1. Open a terminal or command prompt.
1. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On Mac: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
1. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/sublime-sesame.git Sesame
   ```

## Setup

### 1. Set the location of your projects

In the settings file, add the following line to specify the location of your projects.

`Command Palette → Preferences: Settings`

```json
{
    "sesame.path": "~/projects"
}
```

Replace `~/projects` with the path to the directory where your projects are located. Placeholders and variables like `~` and `$HOME` will expanded.

By default, Sesame will discover projects two levels deep: `~/projects/*/*`. If you prefer a different depth:

```json
{
    "sesame.depth": 2
}
```

See [sesame settings](#settings) for more complex setups.


### 2. Add your preferred key bindings (optional)

By default, there is only a key binding defined for opening a project `Ctrl-Alt-o` (Linux/Windows) and `Super-Alt-o` (Mac). Add your preferred key bindings for the other commands, for example:

`Command Palette → Preferences: Key Bindings`

```json
[
    { "keys": ["ctrl+alt+o"], "command": "sesame_open" },
    { "keys": ["ctrl+alt+a"], "command": "sesame_add" },
    { "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
    { "keys": ["ctrl+alt+s"], "command": "sesame_switch" }
]
```

## Commands

The following commands are available via the Command Palette.

| Command           | Description
| :-----------------| :----------
| Sesame: Open      | Open a project.
| Sesame: Add       | Add a project.
| Sesame: Remove    | Remove a project.
| Sesame: Switch    | Switch between projects.

## Settings

`Command Palette → Preferences: Settings`

| Setting          | Type               | Default   | Description
| :----------------| :------------------| :-------- | :----------
| `sesame.path`    | `string\|list`     | The value of a `PROJECTS_PATH` environment variable or `null`    | The location of projects.
| `sesame.depth`   | `integer`          | `2`       | The projects path depth to discover projects.
| `sesame.keymaps` | `boolean`          | `true`    | Enable default key bindings.
| `sesame.vcs`     | `boolean|null`     | `null`    | Set whether to use version control system (VCS) integration for projects.

### sesame.path

- Type: `string | list`
- Default: `PROJECTS_PATH` environment variable or `null`

You can configure the default projects path using the `sesame.path` setting:

```json
{
    "sesame.path": "~/projects"
}
```

If you have multiple projects paths, you can set them using the `PATH` separator (':' for POSIX or ';' for Windows):

```json
{
    "sesame.path": "~/projects:~/work:~/src"
}
```

Alternatively, specify multiple paths as a list:

```json
{
    "sesame.path": [
        "~/projects",
        "~/work",
        "~/src"
    ]
}
```

Moreover, you can use a `PROJECTS_PATH` environment variable to set a default projects path, instead of using the `sesame.path` setting.

For example, on Linux, you could define the variable in `~/.profile` (a system restart may be required):

```sh
export PROJECTS_PATH=~/projects
```

The `sesame.path` setting will override the `PROJECTS_PATH` environment variable value.

**Multiple paths**

The `sesame.path` setting also accepts a list of complex paths with different configurations for each path, for example:

```json
{
    "sesame.depth": 2,
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
}
```

In this example, we have set the default depth to `2`, which will be applied to any project paths that do not have a specific depth defined.

Additionally, we have configured two specific project paths:

1. The path `~/projects` has a customized depth of `1`, which means projects under this path will be organized in a single directory level.

1. The path `~/vendor` has the setting `"vcs": true`, which indicates that only folders that are are version controlled (VCS) are included for this path.

### sesame.depth

- Type: `int`
- Default: `2`

By default, projects are discovered two level deep within the projects path: `~/projects/*/*`

This maps nicely to `vendor/name` which is typical of endpoints on services like GitHub. For example, if your projects are structured as follows:

```
❯ ~/projects
├── laravel
│   ├── fortify
│   ├── framework
│   ├── jetstream
│   ├── passport
│   └── vite-plugin
├── sublimelsp
│   └── LSP
└── wbond
    ├── package_control
    └── packagecontrol.io
```

Sesame will discover and prompt you with the following items:

```
laravel/fortify
laravel/framework
laravel/jetstream
laravel/passport
laravel/vite-plugin
sublimelsp/LSP
wbond/package_control
wbond/packagecontrol.io
```

When setting the depth to `1`, Sesame will discover and prompt you with the following:

```
laravel
sublimelsp
wbond
```

If you prefer to organize your projects on a single directory level, you can set the depth to `1`:

1. `Command Palette → Preferences: Settings`
1. Add the following configuration:
   ```json
   {
       "sesame.depth": 1
   }
   ```

### sesame.vcs

- Type: `null|boolean`
- Default: `null`

The `sesame.vcs` setting allows you to control the inclusion of version control system (VCS) integration for projects in Sesame. Here are the available options:

- `null`: This setting includes both version-controlled and non-version-controlled projects. Projects with and without VCS integration will be considered.
- `true`: With this setting, only version-controlled projects will be included. Projects without VCS integration will be excluded.
- `false`: This setting excludes version-controlled projects. Only projects without VCS integration will be considered.

`Command Palette → Preferences: Settings`

```json
{
    "sesame.vcs": true
}
```

## Custom commands

All of the commands accept `path`, `depth`, and `vcs` arguments. For example, to create a custom Command Palette item, create or edit the user default commands file, e.g. `User/Default.sublime-commands`, with a new command definition passing the path as an argument:

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

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
