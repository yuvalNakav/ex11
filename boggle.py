import board


def handle_game() -> None:
    """Handles actual gameplay"""
    _board = board.Board()
    _board.run()


if __name__ == "__main__":
    handle_game()
