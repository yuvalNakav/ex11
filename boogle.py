import tkinter as tki
import boggle_board_randomizer
import boogle_board

def handle_game():
    _board = boogle_board.BoggleBoard()
    _board.run()
    # print(_board.run())


if __name__ == '__main__':
    handle_game()
