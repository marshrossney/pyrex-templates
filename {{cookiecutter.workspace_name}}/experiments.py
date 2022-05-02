import json
import os
import pathlib

import nox

nox.options.sessions = []
nox.options.error_on_external_run = True
nox.options.report = True

with pathlib.Path(__file__).with_name(".pyrex_workspace.json").open("r") as file:
    pyrex_workspace = json.load(file)
workspace_root = pathlib.Path(pyrex_workspace["workspace_root"]).resolve()
package_dir = workspace_root / "{{cookiecutter.package_name}}"


@nox.session(python="{{cookiecutter.__python_version}}")
def example(session):
    """An example of how to use nox & poetry to test & execute a python script."""
    assert os.path.exists(
        workspace_root / "poetry.lock"
    ), "lockfile not found! Run 'poetry update --lock' first"
    session.run_always("poetry", "install", "-v", external=True)
    session.run(
        "poetry",
        "run",
        "pytest",
        "--pyargs",
        "{{cookiecutter.package_name}}",
        external=True,
    )
    session.run(
        "poetry",
        "run",
        "python",
        str(package_dir / "main.py"),
        external=True,
    )
