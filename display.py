from rich.console import Console
from rich.panel import Panel

frames = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]

class Display:
    def __init__(self):
        self.console = Console()

    def render(self, word_state, wrong_guesses):
        # goede frame pakken
        frame = frames[min(len(wrong_guesses), len(frames) - 1)]

        body = (
            f"{frame}\n"
            f"[bold green]Word:[/bold green] {word_state}\n"
            f"[bold red]Misses:[/bold red] {", ".join(wrong_guesses)}\n"
            f"[bold yellow]Tries left:[/bold yellow] {max(0, 6 - len(wrong_guesses))}/6\n"
        )

        panel = Panel(body, expand=False)
        self.console.clear()
        self.console.print(panel)