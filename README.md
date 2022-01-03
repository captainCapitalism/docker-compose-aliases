# docker-compose-aliases
CLI that shortens commonly used docker and docker-compose commands.

# Installation
1. Build package with `source scripts/build.sh`

2. Install package:
    - Using `pipx` (recommended): `source scripts/install.sh`.
      - Why `pipx`? 
      - It creates separate environment for installed packages, so they don't 
        interfere with system `python`.
    - Using pip: `pip install dist/app-0.1.03-none-any.whl.
   
# Usage
1. Run `dx` or `dx --help` to see available commands
2. Run `dx $command --help` to see available arguments. Ex. `dx u --help`

# Customization / Development

1. Spin up project
```
docker-compose up -d
```
or (if installed0)
```
dx u
```
2. Customize names or commands content. You can read short introduction to `typer`
   [here](https://typer.tiangolo.com/tutorial/commands/).
3. Customize main command alias at `pyproject.toml/[tool.poetry.scripts]`
You can declare more than one script/path in `pyproject.toml`.

4. Apply changes with 
```
source scripts/update.sh
```
