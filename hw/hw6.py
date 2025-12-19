# Библиотека rich предназначена для красивого и удобного вывода информации в консоль
from rich.console import Console

console = Console()
console.print("[green]Можно идти[/green]")
console.print("[yellow]Приготовься[/yellow]")
console.print("[red]Стой[/red]")

name = "Kamila"
age = 16

console.print(f"[bold]Имя:[/bold] {name}")
console.print(f"[bold]Возраст:[/bold] {age}")