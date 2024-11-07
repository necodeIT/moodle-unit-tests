import click
import driver
from click_spinner import spinner
from utils import baseline_file_exists

@click.group(invoke_without_command=True)
@click.pass_context
def test(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@test.command()
@click.argument("name", type=click.STRING, required=True)
def create(name: str) -> None:
    """
    Creates and sets up folder structure for a new test batch.
    """

    driver.create_test_batch(name)

    

@test.command()
def restore() -> None:
    pass