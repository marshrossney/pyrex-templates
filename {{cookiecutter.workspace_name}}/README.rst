===============================
{{cookiecutter.workspace_name}}
===============================

:Authors: ...
:Description: {{cookiecutter.description}}

------------
Installation
------------

Install Python {{cookiecutter.__python_version}} and activate this version of Python in the current shell. If you are using `pyenv <https://github.com/pyenv/pyenv>`_ to manage different Python versions on your system, run the following commands::

    pyenv install {{cookiecutter.__python_version}}
    pyenv activate {{cookiecutter.__python_version}}

Install `Poetry <https://python-poetry.org/>`_ using `pipx <https://pypa.github.io/pipx/>`_::

    python -m pip install pipx
    python -m pipx ensurepath
    pipx install poetry

Now ask Poetry to create a dedicated virtual environment in which to install this package::

    poetry install

------------------------------------
Running experiments using tox or nox
------------------------------------

Install tox or nox using pipx::

    pipx install tox
    pipx install nox

