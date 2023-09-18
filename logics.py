from typing import *
import tkinter as tki
import cell

with open("boggle_dict.txt", "r") as txt_file:
    words = [word.split("\n")[0] for word in txt_file.readlines()]


def check_valid_next_press(curr_cell: cell.Cell, next_cell: cell.Cell) -> bool:
    """Validates press by current cell and next cell's locations"""
    if curr_cell:
        return (
            -1 <= curr_cell.row - next_cell.row <= 1
            and -1 <= curr_cell.column - next_cell.column <= 1
        )
    return True


def check_word_validity(word: tki.StringVar, path: List[Tuple[int, int]]):
    if len(path) >= 1:  # there is a word
        return word.get() in words
    else:
        return False
