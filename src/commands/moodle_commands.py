import click
import inquirer
import driver
import webbrowser
import moodle as mdl
from click_spinner import spinner
from constants import *
from utils import get_service_ip

@click.group(invoke_without_command=True)
@click.pass_context
def moodle(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@moodle.command()
@click.argument("version", type=click.Choice(mdl.get_releases()), required=False)
def init(version: str | None) -> None:
    """
    Downloads and sets up a local moodle instance.
    """

    if version is None:
        choice = inquirer.prompt(
            [
                inquirer.List(
                    "version",
                    message="Select moodle version",
                    choices=mdl.get_releases(),
                )
            ]
        )

        version = choice["version"]

    config = driver.Config(version)
    driver.save_config(config)

@moodle.command()
def run() -> None:
    """
    Runs the moodle instance.
    """
    click.echo("Running moodle...")
    with spinner():
        driver.launch_docker_compose()
        service_ip = get_service_ip(MOODLE_CONTAINER_NAME)

    path = f"http://{service_ip}:{MOODLE_HTTP_PORT}"
    click.echo(f"Moodle is running at {path}")

    webbrowser.open(path)


@moodle.command()
def stop() -> None:
    """
    Stops the moodle instance.
    """
    click.echo("Stopping moodle...")
    with spinner():
        driver.stop_docker_compose()