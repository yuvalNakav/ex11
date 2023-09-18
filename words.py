import tkinter as tki
import tkinter.ttk as ttk


class Words:
    """Words component class.
    Displays valid founded words
    """
    def __init__(self, root):
        """Init function"""
        self._root = root
        self.words = tki.StringVar(self._root)
        self.word_list = ttk.Label(self._root, textvariable=self.words)
        self.word_list.configure(padding=4)
        self.word_list.grid(row=6, columnspan=4)

    def add_word(self, word: str) -> None:
        """Adds a new word to used words"""
        words = self.words.get().split("\n")
        if word not in words:
            self.words.set(value=self.words.get() + "\n" + word)

    def reset(self) -> None:
        """Resets used words for a new game"""
        self.words.set(value="")

