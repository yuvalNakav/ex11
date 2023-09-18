import tkinter as tki
import tkinter.ttk as ttk


class CurrentWord:
    """
    Input component.
    Handles input reset
    """
    def __init__(self,root: tki.Tk, style: ttk.Style):
        """
        init method.
        places current word in grid
        """
        self.curr_word = tki.StringVar()
        self._root = root
        self._input = ttk.Label(textvariable=self.curr_word)
        self.path = []
        # init style
        self.style = style
        self.style_name = "TLabel.input"
        self.style.configure(self.style_name, foreground="white")
        self._input.grid(row=0, columnspan=2)

    def reset(self):
        """Handles input reset"""
        self.curr_word.set("")
        self.path = []
