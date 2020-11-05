# {{ cookiecutter.project_name }}


{{ cookiecutter.project_short_description }}

Original repository: [https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})

Author: {{ cookiecutter.full_name }} 
  ([{{ cookiecutter.email }}](mailto:{{ cookiecutter.email }}))


# License
{% set is_open_source = cookiecutter.license != 'Not open source' -%}
{% if is_open_source %}
{{ cookiecutter.license }} -- see [LICENSE](LICENSE)
{% else %}
Not open source -- see [LICENSE](LICENSE)
{% endif %}
