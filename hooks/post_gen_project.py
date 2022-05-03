import pathlib
import shutil

WORKSPACE_PATH = "{{cookiecutter.workspace.relpath}}"
REQUIRED_FILES = {{cookiecutter.experiment.files}}


for file in REQUIRED_FILES:
    src = pathlib.Path(WORKSPACE_PATH).joinpath(file)
    dest = pathlib.Path(".").joinpath(file)

    dest.parent.mkdir(exist_ok=True, parents=True)
    shutil.copy(src, dest)
