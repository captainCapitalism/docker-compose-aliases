import typer
import os

app = typer.Typer()


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


app.command(name="u")(up)
app.command(name="d")(down)
app.command(name="r")(reset)
if __name__ == "__main__":
    app()
