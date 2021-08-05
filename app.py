from flask import Flask
import click
import glob, os
import colorama
import struct
from Crypto.Cipher import AES
from Wii.title import Title
colorama.init()
app = Flask(__name__)

@click.group()
def cli():
    pass

@cli.command()
def generate_listings():
    click.echo(click.style("Generating Listings...", fg="green"))
    os.chdir("titles/")
    is_first = True
    output = {}
    for file in glob.glob("*.wad"):
        if is_first:
            is_first = False
            click.echo(click.style(f"Creating listing for titles/{file}", fg="green"))
        else:
            click.echo(click.style(f"{colorama.ansi.AnsiCursor.UP(1)}Creating listing for titles/{file}", fg="green"), nl=False)
        with open(file, "rb") as f:
            title = Title(f.read()) # Get the contents of the title
            title._dumpDir("temp/")
        with open("temp/00000000.app") as f:
            # Now we can get the title's name:
            f.seek(0x9D)
            title = f.read(84)
            title = title.decode("utf-8")
            print(title)


            



if __name__ == "__main__":
    cli()