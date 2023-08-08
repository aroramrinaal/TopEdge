import typer
import psutil


app = typer.Typer()

@app.command()
def main():
    typer.echo("Welcome to TopEdge - The Modern CLI System Monitor")

def format_bytes(bytes_num):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_num < 1024:
            return f"{bytes_num:.2f} {unit}"
        bytes_num /= 1024


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

@app.command()
def memory():
    mem_info = psutil.virtual_memory()
    swap_info = psutil.swap_memory()

    typer.echo("Memory Usage:")

    # Total Memory
    typer.echo(f"  Total Memory: {format_bytes(mem_info.total)}")

    # Available Memory
    typer.echo(f"  Available Memory: {format_bytes(mem_info.available)}")

    # Used Memory
    used_memory = mem_info.total - mem_info.available
    typer.echo(f"  Used Memory: {format_bytes(used_memory)}")

    # Memory Usage Percentage
    memory_usage_percent = mem_info.percent
    typer.echo(f"  Memory Usage Percentage: {memory_usage_percent}%")

    # Swap Memory (if available)
    if swap_info:
        typer.echo("\nSwap Memory:")
        typer.echo(f"  Total Swap Memory: {format_bytes(swap_info.total)}")
        typer.echo(f"  Used Swap Memory: {format_bytes(swap_info.used)}")
        typer.echo(f"  Free Swap Memory: {format_bytes(swap_info.free)}")


if __name__ == "__main__":
    app()
