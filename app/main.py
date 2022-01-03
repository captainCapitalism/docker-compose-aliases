import os
import typing

import typer

app = typer.Typer(
    no_args_is_help=True,
)


def generate_options(
    name: str,
    short_name: str = None,
) -> typing.Tuple[str, str, str, str]:
    return (
        f"--{name}",
        f"-{short_name or name[0]}",
        f"--no-{name}",
        f"-no-{short_name or name[0]}",
    )


build_option = typer.Option(
    False,
    *generate_options("build"),
)


@app.command()
def up(
    build: bool = build_option,
):
    options = ""
    if build:
        options = f"{options} --build"

    os.system(f"docker-compose up -d{options}")


@app.command()
def down():
    os.system("docker-compose down")


@app.command(help="down && up")
def reset(
    build: bool = build_option,
):
    down()
    up(build)


@app.command(
    name="rx",
    help="stop && rm && system prune",
)
def remove_containers(
    system_prune: bool = typer.Option(
        True,
        *generate_options("prune"),
    )
):
    typer.echo("Stopping containers.")
    os.system("docker stop $(docker ps -aq)")
    typer.echo("Removing containers.")
    os.system("docker rm $(docker ps -aq)")
    if system_prune:
        prune(everything=False)


@app.command(
    name="px",
    help="system prune",
)
def prune(
    everything: bool = typer.Option(
        False, *generate_options("all"), help="Prune all and prune volumes."
    )
):
    options = ""
    if everything:
        options = f"{options} --all"
    os.system(f"docker system prune{options}")
    if everything:
        os.system(f"docker volume prune")


app.command(name="u", help="Alias for `up`")(up)
app.command(name="d", help="Alias for `down`")(down)
app.command(name="r", help="Alias for `reset`")(reset)

if __name__ == "__main__":
    app()
