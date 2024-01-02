# 🍪 A up-to-date Cookiecutter template for MLOps

---

Inspired by the [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) template. This
template has been updated to better fit machine learning-based projects and is being used as the core template in
this [MLOps course](https://github.com/SkafteNicki/dtu_mlops).

## Requirements to use the template:

* Python 3.10
* Cookiecutter v2.4.0

## Start a new project

```bash
cookiecutter https://github.com/SkafteNicki/mlops_template
```

and input starting values for the project.

To commit as a new GitHub repository afterwards

```bash
cd <project_name>
git init
git add .
git commit -m "init cookiecutter project"
git push
```

## The stack

🐍 Python projects using `pyproject.toml` <img src="icons/python.svg" width="20" height="20">

🔥 Models in `pytorch` <img src="icons/pytorch.svg" width="20" height="20">

📄 Documentation in `mkdocs` <img src="icons/markdown.svg" width="20" height="20">

👕 Linting and formatting with `ruff` <img src="icons/ruff.svg" width="20" height="20">

✅ Checking using `pre-commit` <img src="icons/precommit.svg" width="20" height="20">

🛠️ CI with `Github actions` <img src="icons/githubactions.svg" width="20" height="20">
