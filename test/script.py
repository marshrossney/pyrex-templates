from datetime import datetime

from cookiecutter.main import cookiecutter

timestamp_dt = datetime.now()
timestamp = timestamp_dt.strftime("%y%m%dT%H%M%S")


author = dict(
    name="marshrossney",
    profile="https://github.com/marshrossney",
    email="joe@email.com",
)
workspace = dict(
    name="A nice workspace",
    path="test/",
    relpath="../..",
    version="1.0",
)
repo = dict(
    name="repo name",
    relpath="../../../",
    url="repo url",
    branch="repo branch",
    commit="commit sha1",
    is_clean="yes",
)
experiment = dict(
    name="a really nice experiment about bees",
    dirname=timestamp,
    path=f"test/experiment/{timestamp}/",
    timestamp=timestamp,
    timestamp_pretty=timestamp_dt.strftime("%c"),
    files=["file1.txt", "folder/file2.txt"],  # relative to workspace
    commands=["command 1", "command 2"],
)

extra_context = dict(
    author=author, workspace=workspace, repo=repo, experiment=experiment
)

cookiecutter(
    "../",
    output_dir="experiments/",
    no_input=True,
    extra_context=extra_context,
)
