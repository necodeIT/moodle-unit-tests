import sys
import os
import click
from click_spinner import spinner
from setup import install_moodle, get_moodle_versions, get_repo
from moodle import MOODLE_PATH
import inquirer 

if not os.path.exists(MOODLE_PATH):
    click.echo('Initializing...')
    with spinner():
        get_repo()

if sys.version_info[0:2] != (3, 12):
    raise Exception('Requires python 3.12')


    
@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        
@main.command()
@click.argument('version', type=click.Choice(get_moodle_versions()), required=False)
def init(version: str|None) -> None:
    """
    Downloads and sets up a local moodle instance.
    """
    
    if version is None:
        choice = inquirer.prompt([
            inquirer.List('version', message='Select moodle version', choices=get_moodle_versions())
        ])
        
        version = choice['version']
    
    click.echo(f'Installing moodle version {version}...')
    with spinner():
        install_moodle(version)
        
    
@main.command()
def run() -> None:
    """
    Runs the moodle instance.
    """
    click.echo('Running moodle...')
    pass
    
if __name__ == '__main__':
    main.no_args_is_help = True;
    main()