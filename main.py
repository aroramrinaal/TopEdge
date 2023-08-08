import typer

app = typer.Typer()

@app.command()
def main():
    typer.echo("Welcome to TopEdge - The Modern CLI System Monitor")

if __name__ == "__main__":
    app()
