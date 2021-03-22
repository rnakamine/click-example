import click


@click.group()
def cli():
    pass


@cli.command()
def command1():
    click.echo('execute command1')


@cli.command()
def command2():
    click.echo('execute command2')


if __name__ == '__main__':
    cli()
