==========================================
{{ cookiecutter.experiment.name | title }}
==========================================

-----------------------
Running this experiment
-----------------------

1. Clone the repository ``git clone {{ cookiecutter.repo.url }}``
2. Follow the installation instructions provided `here <{{ cookiecutter.workspace.relpath }}/README.rst#Installation>`_
3. Navigate to this directory (you may have to ``git checkout`` this branch)
4. Inside this directory, run ``git checkout {{cookiecutter.repo.commit}}``
5. Run the following commands:

.. code:: sh

{% for cmd in cookiecutter.experiment.commands -%}
{{ cmd | indent(4, True) }}
{% endfor %}


----------------------
Additional information
----------------------

Experiment created on {{ cookiecutter.experiment.timestamp_pretty }} by `{{ cookiecutter.author.name }} <{{ cookiecutter.author.profile }}>`_.

The state of the git working tree can be examined in ``pyexp.log``.

