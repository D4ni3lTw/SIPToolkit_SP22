from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 11)]

with console.status("[bold green]Working on tasks...") as status:
    while tasks:
        print("\n")
        task = tasks.pop(0)
        # console.log(f"{task} Start")
        # print('task')
        sleep(1)
        console.log(f"{task} complete")