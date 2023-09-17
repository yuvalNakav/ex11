import tkinter as tki
import tkinter.ttk as ttk
import boggle_board_randomizer
import boggle as controller
import boogle_cell
import boggle_input
import boogle_words
import boggle_button
import score
import gui_helpers as helper
import boggle_logics as logics
import timer
import tkinter.messagebox as messagebox


class BoggleBoard:
    def __init__(self):
        root = tki.Tk()
        root.title = "Boogle"
        self._root = root
        self.board = boggle_board_randomizer.randomize_board()
        self.curr_cell = None
        self.paths = []
        self.style = ttk.Style()
        self._input = boggle_input.Input()
        self.score = score.Score(self._root)
        self.timer = timer.Timer(self._root, self.on_game_end)
        self.check_button = boggle_button.BoggleButton(
            self._root, self.check_word, "Check", 1, 3, "SeaGreen3"
        )
        self.delete_button = boggle_button.BoggleButton(
            self._root, self.remove_letter, "Delete", 1, 2, "tomato3"
        )
        self._cells = [
            [
                boogle_cell.Cell(
                    cell, i, j, self._root, self.add_to_curr_word, self.validate_press
                )
                for j, cell in enumerate(row)
            ]
            for i, row in enumerate(self.board)
        ]
        self.used_words = boogle_words.Words(self._root)

    def check_word(self, event):
        if logics.check_word_validity(self._input.curr_word, self._input.path):
            self.used_words.add_word(self._input.curr_word.get())
            self.paths.append(self._input.path)
            self.score.score.set((self.score.score.get() + len(self._input.path) ** 2))
        self._input.restart()
        self.restart_buttons()
        self.curr_cell = None

    def restart_buttons(self):
        for row in self._cells:
            for button in row:
                button.restart()

    def validate_press(self, button):
        if logics.check_valid_next_press(self.curr_cell, button):
            self.curr_cell = button
            return True
        return False

    def add_to_curr_word(self, letter, loc):
        self._input.curr_word.set(value=self._input.curr_word.get() + letter)
        self._input.path.append(loc)
        # self.score.set(self.score.get() + len(self.path) ** 2)
        # print(self.path)

    def remove_letter(self, event):
        if len(self._input.path):
            self._input.curr_word.set(value=self._input.curr_word.get()[:-1]) #todo: check "QU"
            row, col = self._input.path.pop()
            self._cells[row][col].restart()
            if len(self._input.path):
                last_row, last_col = self._input.path[-1]
                self.curr_cell = self._cells[last_row][last_col]
            else:
                self.curr_cell = None

    def on_game_end(self):
        will_continue = messagebox.askyesno(
            title="Game Ended!",
            message=f"Good game! your score was {self.score.score.get()}, would you like to play again?",
        )
        if will_continue:
            self.init_new_game()
        else: # todo: close program
            print("else")
            # self._root.
            # self._root.
            # controller.handle_game()

    def init_new_game(self):
        self.board = boggle_board_randomizer.randomize_board()
        self._cells = [
            [
                boogle_cell.Cell(
                    cell, i, j, self._root, self.add_to_curr_word, self.validate_press
                )
                for j, cell in enumerate(row)
            ]
            for i, row in enumerate(self.board)
        ]
        self.restart_buttons()
        self.timer.restart_timer()

    def run(self):
        self.timer.update_time()
        self._root.mainloop()


# if __name__ == '__main__':
#     print(self.style.theme_names())
#     _board = BoggleBoard(boggle_board_randomizer.randomize_board())
#     _board.run()
