import click
import driver
from click_spinner import spinner
from utils import baseline_file_exists

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
    click.echo("Making sure moodle is running...")
    with spinner():
        driver.launch_moodle()
        driver.sql_dump_baseline()
    
    click.echo(f"Baseline dump created.")

@baseline.command()
def restore() -> None:
    """
    Restores the baseline dump of the moodle database.
    """

    if not baseline_file_exists():
        click.echo("Baseline dump not found. Create one with `create-baseline`.")
        return

    click.echo("Making sure moodle is running...")
    with spinner():
        driver.launch_moodle()
        driver.sql_restore_baseline()
