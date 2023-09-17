import tkinter as tki
import tkinter.ttk as ttk


class Score:
    def __init__(self, root):
        self._root = root
        self.score = tki.IntVar()
        self.score_label = ttk.Label(textvariable=self.score) # todo: add "score:" before actual score
        self.score_label.grid(row=1, column=1)
        # self.score_label.grid(root, row=0, column=2)
