import tkinter as tki
import tkinter.ttk as ttk

class BoggleButton:
    def __init__(self, root, command, text, row, column):
        self.button = ttk.Button(root, text=text)
        self.button.bind("<1>", command)
        self.button.grid(row=row, column=column)
