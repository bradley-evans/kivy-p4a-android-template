import click


@click.group()
def cli():
    """! CLI Entrypoint

    The primary CLI entrypoint. Invoked with `myapp`.
    """
    pass


@cli.command()
def about():
    """! Prints about information.
    """
    click.echo(f"myapp: hello world")
