===================================
Base Template for PyREx Experiments
===================================

This is a mimimal cookiecutter template which receives an input configuration from ``pyrex workspace create``.
The most important feature is the ``.pyrex_workspace.yaml`` file, which is required for PyREx to register the directory as a workspace.

The ``.pyrex_workspace.yaml`` file contains the following fields:

:version: A version to associate with the worksapce. This can be either a decimal number or a shell command which returns a string representation of the workspace version (e.g. by reading from a file or running a command provided by a package manager).
:experiments_file: A *relative* path to a YAML file containing a set of experiment configurations.
:experiments_output_path: A path template where new experiments will be created.

--------------
Path templates
--------------

The following substitutions to the ``experiments_output_path`` string will be made when generating a new experiment:

:``{workspace_root}``: The root directory of the workspace (i.e. where the ``.pyrex_workspace.yaml`` file lives.
:``{workspace_name}``: The name of this directory.
:``{version}``: The workspace version.
:``{repo_root}``: The root of the git working tree.
:``{repo_name}``: The name of the git repository.
:``{branch}``: The current branch.
:``{experiment_name}``: The 'name' of the experiment being created, which is the key that picks it out from the experiments config file.

------------
Useful links
------------

- `PyREx <https://github.com/marshrossney/pyrex>`_ : the tool that uses these templates.
- `Documentation for Cookiecutter <https://cookiecutter.readthedocs.io/>`_ : the package that implements the template generation.
- `Documentation for Jinja <https://jinja.palletsprojects.com/>`_ : Jinja is the underlying templating engine. However, unfortunately Cookiecutter only supports a limited subset of its functionality.
