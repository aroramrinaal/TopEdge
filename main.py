import typer
import psutil

app = typer.Typer()

@app.command()
def main():
    typer.echo("Welcome to TopEdge - The Modern CLI System Monitor")

@app.command()
def cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    typer.echo(f"CPU Usage: {cpu_percent}%")


if __name__ == "__main__":
    app()
