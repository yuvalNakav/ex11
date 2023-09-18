import tkinter as tki
import tkinter.ttk as ttk
import boggle_board_randomizer
import cell
import current_word
import words
import button
import feedback_label
import score
import logics as logics
import timer
import tkinter.messagebox as messagebox
from typing import *


class Board:
    """
    Main boggle component.
    Handles game logics and board layout.
    """
    def __init__(self) -> None:
        """
        Initialization function for Board component
        """
        # init variables
        root = tki.Tk()
        root.title = "Boogle"
        self._root = root
        self.board = boggle_board_randomizer.randomize_board()
        self.curr_cell = None
        self.paths = []
        self.style = ttk.Style()
        # init child components
        self.current_word = current_word.CurrentWord(self._root, self.style)
        self.feedback_label = feedback_label.FeedbackLabel(self._root, self.style)
        self.score = score.Score(self._root)
        self.timer = timer.Timer(self._root, self.on_game_end)
        self.check_button = button.Button(
            self._root, self.check_word, "Check", 1, 3, "SeaGreen3", self.style
        )
        self.delete_button = button.Button(
            self._root, self.delete_cell, "Delete", 1, 2, "tomato3", self.style
        )
        self._cells = [
            [
                cell.Cell(
                    _cell, i, j, self._root, self.add_to_curr_word, self.validate_press, self.feedback_label.set_label, self.style
                )
                for j, _cell in enumerate(row)
            ]
            for i, row in enumerate(self.board)
        ]
        self.used_words = words.Words(self._root)

    def check_word(self, event: tki.Event) -> None:
        """
        Handles complete words.
        appends to used words, sets score and success message
        restarts buttons states, input and curr_cell
        """
        if logics.check_word_validity(self.current_word.curr_word, self.current_word.path):
            self.used_words.add_word(self.current_word.curr_word.get())
            self.paths.append(self.current_word.path)
            self.score.add_to_score(len(self.current_word.path) ** 2)
            self.feedback_label.set_label("Word Added!", "green")
        else:
            self.feedback_label.set_label("Invalid Word", "red")
        self.current_word.reset()
        self.restart_cells()
        self.curr_cell = None

    def restart_cells(self) -> None:
        """Restarts all cells"""
        for row in self._cells:
            for _cell in row:
                _cell.reset()

    def validate_press(self, curr_cell: cell.Cell) -> bool:
        """
        Validates single press using logics module
        :return True if valid, else False
        """
        if logics.check_valid_next_press(self.curr_cell, curr_cell):
            self.curr_cell = curr_cell
            return True
        return False

    def add_to_curr_word(self, letter: str, loc: Tuple[int, int]):
        """Adds a letter to input's current word and cell location to current path"""
        self.current_word.curr_word.set(value=self.current_word.curr_word.get() + letter)
        self.current_word.path.append(loc)

    def delete_cell(self, event: tki.Event) -> None:
        """Removes last letter from input's current word and cell location from current path"""
        if len(self.current_word.path):  # preventing index errors
            row, col = self.current_word.path.pop()
            curr_cell = self._cells[row][col]
            # slicing the last curr_word chars by cell length
            self.current_word.curr_word.set(value=self.current_word.curr_word.get()[:-(len(curr_cell))])
            self._cells[row][col].reset()
            if len(self.current_word.path):
                last_row, last_col = self.current_word.path[-1]
                self.curr_cell = self._cells[last_row][last_col]
            else:
                self.curr_cell = None

    def on_game_end(self) -> None:
        """
        Handles game end.
        initializes a new game if the player chooses to do so.
        Otherwise terminates the window
        """
        will_continue = messagebox.askyesno(
            title="Game Ended!",
            message=f"Good game! your score was {self.score.get_score()}, would you like to play again?",
        )
        if will_continue:
            self.init_new_game()
        else:
            self._root.destroy()

    def init_new_game(self) -> None:
        """
        initializes a new game.
        Resets all cells, input and timer.
        """
        self.board = boggle_board_randomizer.randomize_board()
        self._cells = [
            [
                cell.Cell(
                    _cell, i, j, self._root, self.add_to_curr_word, self.validate_press, self.feedback_label.set_label, self.style
                )
                for j, _cell in enumerate(row)
            ]
            for i, row in enumerate(self.board)
        ]
        self.used_words.reset()
        self.score.reset_score()
        self.restart_cells()
        self.current_word.reset()
        self.timer.restart_timer()
        self.curr_cell = None
        self.feedback_label.set_label("", "white")

    def run(self) -> None:
        """Starts boggle Gameplay"""
        self.timer.update_time()
        self._root.mainloop()


# if __name__ == '__main__':
#     print(self.style.theme_names())
#     _board = BoggleBoard(boggle_board_randomizer.randomize_board())
#     _board.run()
