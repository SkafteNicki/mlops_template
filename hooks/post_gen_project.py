import re
from keyword import iskeyword

project_name = '{{cookiecutter.project_name}}'
if not project_name.isidentifier():
    raise ValueError(
        "\n"
        "Project name must be a valid identifier, meaning that it must be a valid Python name. This means that it must"
        " not start with a number, and must not contain spaces or special characters. In general it is best to use"
        " only (lowercase) letters and underscores."
        "\n"
    )
if iskeyword(project_name):
    raise ValueError('Project name must not be a build-in keyword, as it will cause syntax errors.')
