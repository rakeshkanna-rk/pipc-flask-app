import click

from flaskapp import create_flask
from textPlay.colors import *

title = f"{BLUE}PIPCREATOR FLASK APP{RESET}"

@click.group()
def cli():
    print(title)
    pass

@click.command()
@click.argument('directory')
def create_flask_app(directory):
    create_flask(directory)

cli.add_command(create_flask_app)