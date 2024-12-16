from invoke import task


@task
def template(ctx):
    ctx.run("cookiecutter -f --no-input .")


@task
def requirements(ctx):
    ctx.run("python -m pip install --upgrade pip")
    ctx.run("pip install -r requirements.txt")
