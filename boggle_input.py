import tkinter as tki
import tkinter.ttk as ttk
import gui_helpers as helper


class Input:
    def __init__(self):
        self.curr_word = tki.StringVar()
        self._input = ttk.Label(textvariable=self.curr_word)
        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="white")
        self._input.grid(row=0, columnspan=4)
        # self._input.grid(row=0, columnspan=2) # if well manage to build the input feature
        self.path = []

    def restart(self):
        self.curr_word.set("")
        self.path = []
