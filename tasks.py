from invoke import task, Context


@task
def template(ctx: Context, project_structure: str = "simple", project_manager: str = "pip"):
    """Create a new project from the template."""
    if project_structure == "simple" and project_manager == "pip":
        ctx.run("cookiecutter -f --config-file configs/simple_pip_config.yaml --no-input --verbose .")
    if project_structure == "simple" and project_manager == "uv":
        ctx.run("cookiecutter -f --config-file configs/simple_uv_config.yaml --no-input --verbose .")
    if project_structure == "advance" and project_manager == "pip":
        ctx.run("cookiecutter -f --config-file configs/advance_pip_config.yaml --no-input --verbose .")
    if project_structure == "advance" and project_manager == "uv":
        ctx.run("cookiecutter -f --config-file configs/advance_uv_config.yaml --no-input --verbose .")

@task
def requirements(ctx: Context):
    """Install project requirements."""
    ctx.run("python -m pip install --upgrade pip")
    ctx.run("pip install -r requirements.txt")


@task
def clean(ctx: Context):
    """Clean up the project."""
    ctx.run("rm -rf repo_name")
    ctx.run("rm -rf simple_repo")
    ctx.run("rm -rf advance_repo")
    ctx.run("rm -rf .pytest_cache")
    ctx.run("rm -rf .ruff_cache")
