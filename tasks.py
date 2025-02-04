from invoke import task, Context


@task
def template(ctx: Context):
    """Create a new project from the template."""
    ctx.run("cookiecutter -f --no-input --verbose .")

@task
def simple(ctx: Context):
    """Create a new project from the template."""
    ctx.run("cookiecutter -f --config-file configs/simple_config.yaml --no-input .")

@task
def advance(ctx: Context):
    """Create a new project from the template."""
    ctx.run("cookiecutter -f --config-file configs/advance_config.yaml --no-input --verbose .")


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
