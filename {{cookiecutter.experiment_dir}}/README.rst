============================================
{{ cookiecutter._experiment.title | title }}
============================================

-----------------------
Running this experiment
-----------------------

1. Clone the repository
2. Follow the installation instructions provided `here <{{ cookiecutter._path.to_workspace_root }}/README.rst#Installation>`_
3. Navigate to this directory (you may have to ``git checkout`` this branch)
4. Inside this directory, run ``git checkout {{cookiecutter._repository.commit}}``
5. Run the following commands:

.. code:: sh

{% for cmd in cookiecutter._experiment.commands -%}
{{ cmd | indent(4, True) }}
{% endfor %}


***

This experiment was created on {{ cookiecutter._date }} by `{{ cookiecutter._author.name }} <https://github.com/{{ cookiecutter._author.name }}>`_ using `PyRex <https://github.com/marshrossney/pyrex>`.

