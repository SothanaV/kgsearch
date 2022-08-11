import os
import webbrowser

import click
from rich import print

from .app import Search, create_app

__all__ = ["app"]

path = os.path.abspath(os.path.dirname(__file__))


@click.command("start", short_help="Start the app")
@click.argument("arg", type=str)
@click.option("-f", help="Csv file with triples.")
def start(arg, f):

    if arg == "start":
        # lsof -i:9200
        # lsof -i:5000
        # kill -9 <PID>

        app = create_app()

        print("🎉 Starting the app.")
        webbrowser.open(os.path.join("file://" + path, "web/app.html"))
        app.run()

    elif arg == "add":
        Search(file=f).save(path=os.path.join(path, "data/search.pkl"))

    elif arg == "open":
        print("😎 Opening web.")
        webbrowser.open(os.path.join("file://" + path, "web/app.html"))
