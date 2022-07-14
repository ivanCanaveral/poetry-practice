# poetry-practice

Just playing around with poetry

(!) This repo has been developed using vscode ;) and it assumes that the following extensions are installed:
 * Python
 * Pylance
 * pyLint

## Getting Started

```bash
poetry init
```

By default, poetry will create an environment folder outside your project folder. To help VSCode to detect this environment we have two options:

#### Declare your poetry environments path

You can explore poetry config with:

```bash
poetry config --list
```

You can find or modify poetry `cache-dir`and `virtualenvs.path`, which is usually based on your `cache-dir`.

Additionally, you can get poetry's folder with the following command

```bash
where poetry
```

Now we can use this info to update VSCode project config: `File > Preferences > Settings`or `[Ctrl + ,]`. You can update `"python.poetryPath"` variable now. It should be more than enough.

```
A VS Code "workspace" is usually just your project root folder. Workspace settings as well as debugging and task configurations are stored at the root in a .vscode folder.
```


#### Set your dependencies folder inside your project folder:

Just modify the poetry configuration, to make poetry install dependencies in yout project's folder:

```bash
poetry config virtualenvs.in-project true
```

## Installing libraries

```bash
poetry add --dev black
poetry add --dev pylint
poetry add --dev pyright
```

### Pylint

Pylint is a linter for python. It detect programming errors, so this is about functionality.

```bash
pytlint <filename/folder>
```

VS Code will analyze your code automatically.

#### pylint config

We can store pylint config in the `pyproject.toml`.

```toml
[tool.pylint.messages_control]
max-line-length = 79
````

### Black

Black can help you with code formatting. This is just about style.

Use `black --check <filename/folder>` to analyze files. When are sure about the changes, just lauch:

```bash
black <filename/folder>
```

If you're using VS Code, with pyLance extension installed, it will detect and use **black** to format your code.

#### Black config

You can edit black default's passing them through the command line:

```bash
black --check --line-lenght 79 <filename/folder>
```

However, this can get very annoying if you use this tool intensively. In this case, you can always set it in config files.

You can save this configuration within **VS Code Settings** if it is something you are going to use in all your projects. Just add these lines to your settings.json:

```json
    "python.formatting.blackArgs": [
        "--line-length", "79"
    ]
```

But, if you are going to work as part of a team, you may include this configuration in the `pyproject.toml` file:

```toml
[tool.black]
line-length = 79
```

### mypy

Same here:

```bash
mypy <filename/folder>
```

#### mypy config

This library also supports `pyproject.toml` configuration.

```toml
[tool.mypy]
disallow_untyped_defs = True
disallow_any_unimported = True
no_implicit_optional = True
check_untyped_defs = True
warn_return_any = True
show_error_codes = True
warn_unused_ignores = True
```
