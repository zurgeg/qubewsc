from flask import Flask
import click
import glob, os
import colorama
import struct
from Crypto.Cipher import AES
import subprocess
from sys import executable
from pywii.Alameda import Alameda
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
        # Now we summon the almighty PyWii
        os.mkdir("temp")
        subprocess.Popen([executable, "pywii/pywii/pywii-tools/wadunpack.py", file, "temp"])
        banner = Alameda("temp/00000000.app") # 00000000.app always exists in a WAD and is always the banner.
        # Now we get the title name
        title_name = banner.imet.Names[0].decode("utf-8")
        print(title_name)
            



if __name__ == "__main__":
    cli()