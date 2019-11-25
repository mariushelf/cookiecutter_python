# {{ cookiecutter.project_name }}

* Author: {{ cookiecutter.full_name }} 
  ([{{ cookiecutter.email }}](mailto:{{ cookiecutter.email }}))

{{ cookiecutter.project_short_description }}

# License
{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% if is_open_source %}
[{{ cookiecutter.open_source_license }}](https://choosealicense.com/licenses/{{ cookiecutter.open_source_license|lower }})
{% else %}
Not open source.
{% endif %}

