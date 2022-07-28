# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

```{toctree}
---
maxdepth: 2
caption: "Documentation"
hidden:
glob:
---
self
```

```{toctree}
---
maxdepth: 3
caption: "API Reference"
hidden:
---
API Reference <_apidoc/{{ cookiecutter.project_slug }}>
Github repository <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
LICENSE
```


:::{panels}
:container: +full-width text-center
:column: col-lg-4 px-2 py-2
:card:

**[API Reference](_apidoc/{{ cookiecutter.project_slug }}.rst)**
^^^
Full API Documentation

---
**[License](LICENSE)**
^^^
{{ cookiecutter.license }}

---
**[Github](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})**
^^^
[gh:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
:::
