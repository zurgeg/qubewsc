from flask import Flask
import click
import glob, os
import colorama
import struct
from Crypto.Cipher import AES
import subprocess
from sys import executable
from pywii.Alameda import Alameda
from pywii.extractwad import extractwad
import json
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
        extractwad(file, "temp")
        os.chdir("temp")
        for filen in glob.glob("*"):
            if not filen in ["certs", "cetk", "footer", "tmd"] and not file.startswith("0000000"):
                # Looks like it's the banner
                filename = filen
        banner = Alameda.Alameda(filename) # 00000000.app always exists in a WAD and is always the banner.
        # Now we get the title name
        title_name = banner.imet.Names[1]
        output[file] = {
            "name": title_name
        } # TODO: What other stuff should we put in here?
    os.chdir("../../") # Take us back to the main folder
    json.dump(output, open("titles/tdb.json", "w"))
    click.echo(click.style("Successfully generated listings!", bold=True, fg="green"))
        
            



if __name__ == "__main__":
    cli()