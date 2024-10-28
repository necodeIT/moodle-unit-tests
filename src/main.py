import sys
import os
import click
from click_spinner import spinner
from constants import *
from utils import *
from commands.baseline_commands import *
from commands.moodle_commands import *

if sys.version_info[0:2] != (3, 12):
    raise Exception("Requires python 3.12")


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

main.add_command(moodle)
main.add_command(baseline)

if __name__ == "__main__":
    main.no_args_is_help = True
    main()
