import tkinter as tki
import tkinter.ttk as ttk


class Score:
    """
    Score component class.
    Handles score getter and setter
    """
    def __init__(self, root: tki.Tk):
        """Initializes new Score component."""
        self._root = root
        self._score = tki.StringVar(value="score: 0")
        self.score_label = ttk.Label(textvariable=self._score)  # todo: add "score:" before actual score
        self.score_label.grid(row=1, column=1)
        # self.score_label.grid(root, row=0, column=2)

    def add_to_score(self, score_to_add: int):
        """Sets score's StringVar by adding the new score to general"""
        old_score = int(self._score.get().split("score: ")[1])
        print("old_score", old_score)
        self._score.set(value=f"score: {old_score + score_to_add}")

    def get_score(self) -> int:
        """Gets score's numerical value."""
        return int(self._score.get().split("score: ")[1])

    def reset_score(self) -> None:
        """Resets score to 0 for new games."""
        self._score.set(value="score: 0")
