import subprocess

subprocess.run(
    [
        "poetry",
        "init",
        "--name",
        "{{cookiecutter.package_name}}",
        "--description",
        "{{cookiecutter.description|default('no description provided', true)}}",
        "--dev-dependency",
        "pytest",
        "--dev-dependency",
        "flake8",
        "--dev-dependency",
        "black",
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
subprocess.run(
    [
        "poetry",
        "install",
    ]
)
