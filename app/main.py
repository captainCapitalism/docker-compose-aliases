import os

import typer

app = typer.Typer(
    no_args_is_help=True,
)


@app.command()
def up(build: bool = False):
    options = ""
    if build:
        options = f"{options} --build"

    os.system(f"docker-compose up -d{options}")


@app.command()
def down():
    os.system("docker-compose down")


@app.command()
def reset(build: bool = False):
    down()
    up(build)


@app.command(name="rx")
def remove_containers(
    system_prune: bool = typer.Option(
        False,
        "--prune",
        "-p",
        "--no-prune",
        "-no-p",
    )
):
    typer.echo("Stopping containers.")
    os.system("docker stop $(docker ps -aq)")
    typer.echo("Removing containers.")
    os.system("docker rm $(docker ps -aq)")
    if system_prune:
        prune()


@app.command(name="px", help="prune")
def prune(
    everything: bool = typer.Option(
        True,
        "--all",
        "-a",
        "--no-all",
        "-no-a",
    )
):
    typer.echo(everything)
    options = ""
    if everything:
        options = f"{options} --all"
    os.system(f"docker system prune{options}")
    if everything:
        os.system(f"docker volume prune")


app.command(name="u")(up)
app.command(name="d")(down)
app.command(name="r")(reset)

if __name__ == "__main__":
    app()
