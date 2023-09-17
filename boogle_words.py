import tkinter as tki
import tkinter.ttk as ttk


class Words:
    def __init__(self, root):
        self._root = root
        self.words = tki.StringVar(self._root)
        self.word_list = ttk.Label(self._root, textvariable=self.words)
        self.word_list.configure(padding=4)
        self.word_list.grid(row=6, columnspan=4)

    def add_word(self, word):
        words = self.words.get().split("\n")
        if word not in words:
            # print("!!!!!!!!")
            self.words.set(value=self.words.get() + "\n" + word)
            # print(self.words.get())
