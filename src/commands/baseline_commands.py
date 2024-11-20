import click
import driver
from click_spinner import spinner

@click.group(invoke_without_command=True)
@click.pass_context
def baseline(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@baseline.command()
def create() -> None:
    """
    Creates a baseline dump of the moodle database.
    """
    with spinner():
        driver.sql_dump_baseline()
    
    click.echo(f"Baseline dump created.")

@baseline.command()
def restore() -> None:
    """
    Restores the baseline dump of the moodle database.
    """

    with spinner():
        driver.sql_restore_baseline()
