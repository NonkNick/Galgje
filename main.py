from hangman import HangmanGame
from display import Display
from rich.console import Console


#
def main():
    # maak een game klasse aan voor alle logica en een display klasse om het weer te geven, rich gebruiken voor makkelijkere weergave
    console = Console()
    game = HangmanGame()
    display = Display()

    # infinite loop totdat het spel voorbij is
    while not game.is_game_over():
        display.render(game.get_word_state(), game.get_wrong_guesses())
        game.guess()

    display.render(game.get_word_state(), game.get_wrong_guesses())

    if game.is_win():
        console.print(f"[bold green]You won! The word was: {game.word}[/bold green]")
    else:
        console.print(f"[bold red]You lost! The word was: {game.word}[/bold red]")

if __name__ == "__main__":
    main()