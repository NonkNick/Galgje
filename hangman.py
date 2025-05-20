from rich.console import Console
from random import choice

class HangmanGame:
    def __init__(self):
        self.console = Console()
        self.word = self._wordchoice("Woordlijst.txt")
        self.guess_state = ["_"] * len(self.word)
        self.guesses = []
        self.wrong_guesses = []
        self.max_attempts = 6
        self.win_state = False
        self.game_over = False

    def _wordchoice(self, filepath):
        with open(filepath, "r") as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return choice(words)

    def guess(self):
        while True:
            letter = self.console.input("[bold cyan]Guess a letter or the word:[/bold cyan] ").strip().upper()
            if letter == self.word:
                self.win_state = True
                self.game_over = True
                return

            if len(letter) != 1:
                self.console.print("[bold red]Enter one character or guess the word.[/bold red]")
            elif not letter.isalpha():
                self.console.print("[bold red]Enter a valid character.[/bold red]")
            elif letter in self.guesses:
                self.console.print(f"[bold yellow]You already tried '{letter}'![/bold yellow]")
            else:
                break

        self.guesses.append(letter)
        indexes = [i for i, c in enumerate(self.word) if c == letter]
        if indexes:
            self.console.print(f"[bold green]'{letter}' is correct![/bold green]")
            for i in indexes:
                self.guess_state[i] = letter

            if "".join(self.guess_state) == self.word:
                self.win_state = True
                self.game_over = True
        else:
            self.console.print(f"[bold red]'{letter}' is wrong![/bold red]")
            self.wrong_guesses.append(letter)

            if len(self.wrong_guesses) >= self.max_attempts:
                self.game_over = True

    def get_word_state(self):
        return " ".join(self.guess_state)

    def get_wrong_guesses(self):
        return self.wrong_guesses

    def is_game_over(self):
        return self.game_over

    def is_win(self):
        return self.win_state