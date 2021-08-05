from flask import Flask
import click
import glob, os
import colorama
colorama.init()
app = Flask(__name__)

@click.group()
def cli():
    pass

@cli.command()
def generate_listings():
    click.echo(click.style("Generating Listings...", fg="green"))
    os.chdir("titles/")
    tmds = []
    is_first = True
    for file in glob.glob("*tmd*"):
        if is_first:
            is_first = False
            click.echo(click.style(f"Creating listing for titles/{file}", fg="green"))
        else:
            click.echo(click.style(f"\033[FCreating listing for titles/{file}", fg="green"), nl=False)
        

if __name__ == "__main__":
    cli()