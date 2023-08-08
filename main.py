import typer

app = typer.Typer()

@app.callback()
def main():
    typer.echo("Welcome to TopEdge - The Modern CLI System Monitor")

# Rest of your code for cpu, memory, and other commands

if __name__ == "__main__":
    app()
