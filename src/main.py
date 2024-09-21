import sys
import os
import click
from click_spinner import spinner
import driver
import moodle as mdl
import inquirer

if sys.version_info[0:2] != (3, 12):
    raise Exception("Requires python 3.12")


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
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


@main.command()
def run() -> None:
    """
    Runs the moodle instance.
    """
    click.echo("Running moodle...")
    with spinner():
        driver.launch_moodle()


if __name__ == "__main__":
    main.no_args_is_help = True
    main()
