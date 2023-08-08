# Sesame - A Quick Way to Manage Projects and Folders in Sublime Text

Sesame is a powerful Sublime Text plugin that simplifies the process of opening, adding, switching, and removing projects and folders. Its intuitive features provide a seamless experience for organizing your work.

<p>
    <a href="https://packagecontrol.io/packages/Sesame"><img alt="Downloads" src="https://img.shields.io/packagecontrol/dt/Sesame.svg?style=flat-square"></a>
</p>

![Ali Baba overhearing one of the thieves saying "Open Sesame"](open-sesame.webp)

## The Name "Sesame"

The name "Sesame" is a clever play on the famous phrase "[Open Sesame](https://en.wikipedia.org/wiki/Open_sesame)" from the timeless tale of "[Ali Baba and the Forty Thieves](https://en.wikipedia.org/wiki/Ali_Baba_and_the_Forty_Thieves)," found in Antoine Galland's version of the classic collection [One Thousand and One Nights](https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights). In the story, this magical phrase is used to open the mouth of a cave, revealing the hidden treasure of forty thieves.

## Quick Introduction to Sesame

To learn more about Sesame and its usage, check out our [blog post](https://blog.gerardroche.com/2023/05/19/sesame-a-sublime-text-plugin/). It provides a concise and informative introduction to help you get started.

By using Sesame, you can streamline your project management workflow in Sublime Text, making it easier to focus on your creative tasks and boost your productivity.

## Installation

**Method 1: Using Package Control**

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "Sesame" and select it from the list of available packages.

**Method 2: Manual Installation**

1. Visit the [Sesame GitHub repository](https://github.com/gerardroche/sublime-sesame).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "Sesame" folder from the extracted ZIP and paste it into the Packages folder.

**Method 3: Manual Git Repository Installation**

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/sublime-sesame.git Sesame
   ```

## Setup

To get started with Sesame, follow these simple setup instructions:

### 1. Set the Location of Your Projects

Open Sublime Text and go to `Command Palette → Preferences: Settings`.

In the settings file, add the following line to specify the location of your projects:

```json
{
    "sesame.path": "~/projects"
}
```

Replace `"~/projects"` with the actual path to the directory where your projects are located.

### 2. Add Your Preferred Key Bindings

Next, you can add your preferred key bindings for Sesame commands.

Open Sublime Text and go to `Command Palette → Preferences: Key Bindings`.

In the key bindings file, add the following lines to configure the key bindings:

```json
[
    { "keys": ["ctrl+alt+o"], "command": "sesame_open" },
    { "keys": ["ctrl+alt+a"], "command": "sesame_add" },
    { "keys": ["ctrl+alt+r"], "command": "sesame_remove" },
    { "keys": ["ctrl+alt+s"], "command": "sesame_switch" }
]
```

These key bindings will allow you to perform the following actions with Sesame:

- `Ctrl + Alt + o`: Open a project.
- `Ctrl + Alt + a`: Add a project.
- `Ctrl + Alt + r`: Remove a project.
- `Ctrl + Alt + s`: Switch between projects.

Feel free to adjust the key bindings to suit your preferences.

With the setup completed, you can now start using Sesame to manage your projects and folders effortlessly in Sublime Text. Enjoy a smoother and more organized development experience!

## Commands

The Sesame plugin provides several commands that you can access from the command palette. To use them, open Sublime Text and go to `Command Palette → Command`.

| Command           | Description
| :-----------------| :----------
| Sesame: Open      | Open a project.
| Sesame: Add       | Add a project.
| Sesame: Remove    | Remove a project.
| Sesame: Switch    | Switch between projects.

These commands allow you to easily manage your projects and folders in Sublime Text using Sesame. You can open, add, remove, and switch between projects with just a few clicks, streamlining your workflow and enhancing your productivity.

## Settings

Below are the available settings that you can configure for Sesame. To access them, open Sublime Text and go to `Command Palette → Preferences: Settings`.

| Setting          | Type            | Default                               | Description
| :------          | :---            | :------                               | :----------
| `sesame.path`    | String or List  | `PROJECTS_PATH` environment variable. | Projects locations.
| `sesame.depth`   | Integer         | `2`                                   | Set the depth for organizing projects.
| `sesame.keymaps` | Boolean         | `true`                                | Enable default key bindings.
| `sesame.vcs`     | Boolean or Null | `null`                                | Set whether to use version control system (VCS) integration for projects.

### sesame.path

You can configure the default projects path for Sesame using the `sesame.path` setting:

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

Alternatively, you can specify multiple paths as a list:

```json
{
    "sesame.path": [
        "~/projects",
        "~/work",
        "~/src"
    ]
}
```

Moreover, you can use a `PROJECTS_PATH` environment variable to set a default projects path. Instead of using the `sesame.path` setting, you can define the `PROJECTS_PATH` variable in the appropriate system configuration file. For example, on Linux, you can edit `~/.profile` and add the following line (a system restart may be required):

```sh
export PROJECTS_PATH=~/projects
```

By using the `sesame.path` setting or defining the `PROJECTS_PATH` environment variable, you can easily manage your projects and folders with Sesame, and ensure that it navigates to the correct location to locate your projects efficiently. This flexibility allows you to adapt Sesame to your preferred workflow and environment.

#### Multiple Project Paths

If you have multiple project paths configured, you can customize the depth and other settings on a path-by-path basis using the following approach. A path with no specific setting will fallback to the root setting.

To achieve this, use the following configuration in Sublime Text:

```json
{
    "sesame.depth": 2,
    "sesame.path": [
        {
            "path": "~/projects/a",
            "depth": 1
        },
        {
            "path": "~/projects/b",
            "vcs": true
        }
    ]
}
```

In this example, we have set the default depth to `2`, which will be applied to any project paths that do not have a specific depth defined.

Additionally, we have configured two specific project paths:

1. The path `~/projects/a` has a customized depth of `1`, which means projects under this path will be organized in a single directory level.

2. The path `~/projects/b` has the setting `"vcs": true`, which indicates that version control system (VCS) integration is enabled for projects under this path.

By utilizing this flexible configuration, you can tailor Sesame's behaviour for each project path individually, ensuring that each project is managed according to its specific requirements. This allows for a more personalized and efficient project management experience in Sublime Text.

### sesame.depth

Projects are located using the pattern `*/*`, for example, `vendor/name`.

If you prefer to organize your projects on a single directory level, you can set the depth to `1`:

The default depth is `2`.

To change the depth, follow these steps in Sublime Text:

1. Open the Command Palette: `Command Palette → Preferences: Settings`.

2. Add the following configuration to the settings file:

```json
{
    "sesame.depth": 1
}
```
### sesame.vcs

The `sesame.vcs` setting allows you to control the inclusion of version control system (VCS) integration for projects in Sesame. Here are the available options:

- `null`: This setting includes both version-controlled and non-version-controlled projects. Projects with and without VCS integration will be considered.
- `true`: With this setting, only version-controlled projects will be included. Projects without VCS integration will be excluded.
- `false`: This setting excludes version-controlled projects. Only projects without VCS integration will be considered.

To configure the `sesame.vcs` setting, open Sublime Text and go to `Command Palette → Preferences: Settings`. Add the desired value to the setting like this:

```json
{
    "sesame.vcs": true
}
```

## Custom Sesame Commands

You can add custom commands for Sesame by defining new key bindings and adding them to the Command Palette.

### Key Bindings

To create a custom key binding for the `sesame_open` command, follow these steps:

1. Open Sublime Text and go to `Command Palette → Preferences: Key Bindings`.

2. Add the following JSON configuration to create the new key binding:

```json
[
    {
        "keys": ["ctrl+alt+v"],
        "command": "sesame_open",
        "args": {
            "path": "~/vendor"
        }
    }
]
```

In this example, we have assigned the `sesame_open` command to the key combination `Ctrl + Alt + v` and specified the project path as `~/vendor`.

### Command Palette

To add the custom `sesame_open` command to the Command Palette, create a new file named `User/Default.sublime-commands` with the following JSON content:

```json
[
    {
        "caption": "Sesame: Open Vendor",
        "command": "sesame_open",
        "args": {
            "path": "~/vendor"
        }
    }
]
```

With this configuration, the custom command "Sesame: Open Vendor" will be available in the Command Palette. When selected, it will open the project located at the path `~/vendor`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
