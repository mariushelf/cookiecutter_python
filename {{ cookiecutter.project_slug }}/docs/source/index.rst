===================================================
{{ cookiecutter.project_slug }}
===================================================

{{ cookiecutter.project_short_description }}

.. toctree::
   :maxdepth: 2
   :caption: Documentation
   :hidden:
   :glob:

   self

.. toctree::
   :maxdepth: 3
   :caption: API Reference
   :hidden:

   API Reference <_apidoc/{{ cookiecutter.project_slug }}>
   Github repository <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
   LICENSE

.. toctree::
   :maxdepth: 3
   :caption: Contents

   API Reference <_apidoc/{{ cookiecutter.project_slug }}>
   Github repository <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
   LICENSE
