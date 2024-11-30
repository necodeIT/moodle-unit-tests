import click
from moodle_unit_tests.testing import run_test_batch, create_test_batch

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

    create_test_batch(name)

    
@test.command()
@click.argument("name", type=click.STRING, required=True)
def run(name: str) -> None:
    """
    Runs a test batch.
    """
    run_test_batch(name)

