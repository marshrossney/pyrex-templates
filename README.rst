===============
PyREx Templates
===============

This is a WIP collection of `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ templates for use with `PyREx <https://github.com/marshrossney/pyrex>`_.

There are two distinct types of template: **workspace** templates and **experiment** templates.

Workspace Templates
    These contain a hidden file `.pyrex_workspace.yaml` which is required for PyREx to recognise a directory as a workspace, from which experiments can be generated.
    Apart from that, they can be pretty much anything!
    When creating a new workspace, the user will be prompted to input whatever parameters are defined in ``cookiecutter.json``.

Experiment Templates
    These need not contain any config file.
    However, the ``cookiecutter.json`` file should contain a certain set of fields which are passed to cookiecutter when the user runs ``pyrex create``.
    Currently, the user is not prompted for additional inputs, so it is not possible to extend the base configuration, but this will change when cookiecutter 2.0 is released.

Minimal templates can be found at workspaced/base and `experiments/base <https://github.com/marshrossney/pyrex-templates/tree/experiments/base>`_.

