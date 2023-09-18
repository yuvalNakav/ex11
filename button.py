import tkinter as tki
import tkinter.ttk as ttk
from typing import *


class Button:
    """
    General Button
    Command is sent as an argument from parent component.
    """
    def __init__(self, root: tki.Tk, command: Callable, name: str, row: int, column: int, color: str, style: ttk.Style):
        self.color = color
        self.name = name
        self.button = ttk.Button(root, text=self.name)
        self.style_name = f"Custom.TButton.{name}"
        self.style = style
        self.style.configure(self.style_name, foreground=self.color)
        self.button.bind("<1>", command)
        self.button.grid(row=row, column=column)
