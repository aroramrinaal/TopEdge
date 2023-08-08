import typer
import psutil

app = typer.Typer()

@app.command()
def main():
    typer.echo("Welcome to TopEdge - The Modern CLI System Monitor")

@app.command()
def cpu():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    num_cores = psutil.cpu_count(logical=False)
    load_avg = psutil.getloadavg()

    typer.echo("CPU Usage:")
    for core, percent in enumerate(cpu_percent, start=1):
        typer.echo(f"  Core {core}: {percent}%")
    
    typer.echo(f"Total CPU Cores: {num_cores}")

    typer.echo("\nLoad Average:")
    typer.echo(f"  1 Minute: {load_avg[0]:.2f}")
    typer.echo(f"  5 Minutes: {load_avg[1]:.2f}")
    typer.echo(f"  15 Minutes: {load_avg[2]:.2f}")


if __name__ == "__main__":
    app()
