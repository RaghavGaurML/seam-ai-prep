"""Console script for raghav_cookiecutter_python_boilerplate."""

import typer
from rich.console import Console

from raghav_cookiecutter_python_boilerplate import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for raghav_cookiecutter_python_boilerplate."""
    console.print(
        "Replace this message by putting your code into "
        "raghav_cookiecutter_python_boilerplate.cli.main"
    )
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
