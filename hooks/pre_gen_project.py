import pathlib

WORKSPACE_PATH = "{{cookiecutter.workspace.relpath}}"
REQUIRED_FILES = {{cookiecutter.experiment.files}}


for file in REQUIRED_FILES:
    path = pathlib.Path(WORKSPACE_PATH).joinpath(file)
    if not pathlib.Path(WORKSPACE_PATH).joinpath(file).exists():
        raise FileNotFoundError(f"oh no: {file} == {path} not found!")
