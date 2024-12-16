from invoke import task

@task
def template(ctx):
    ctx.run("cookiecutter -f --no-input .")
