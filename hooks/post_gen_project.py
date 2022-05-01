import subprocess

subprocess.run(
    [
        "poetry",
        "init",
        "--name",
        "{{cookiecutter.package_name}}",
        "--description",
        "{{cookiecutter.description|default('no description provided', true)}}",
        "--no-interaction",
        "--quiet",
    ]
)
subprocess.run(
    [
        "poetry",
        "check",
    ]
)
