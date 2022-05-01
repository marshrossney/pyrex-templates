import subprocess

# Check poetry is installed, #TODO check version
subprocess.run(
    [
        "poetry",
        "--version",
        "--quiet",
    ]
)
