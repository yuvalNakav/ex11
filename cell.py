import tkinter as tki
import tkinter.ttk as ttk
from typing import *


class Cell:
    """
    Boggle cell component
    Handles cell inner states and sends changes to board component
    """
    def __init__(self, value:str, row:int, column:int, root:tki.Tk, add_to_curr_word:Callable, validate_press: Callable, set_label: Callable, style:ttk.Style) -> None:
        # init variables
        self._root = root
        self._value = value
        self.row = row
        self.column = column
        self.set_label = set_label
        self._is_pressed = False
        self.add_to_curr_word = add_to_curr_word
        self.validate_press = validate_press
        # style config
        self.style = style
        self.style_name = f"Custom.TButton{self.row}{self.column}"
        self.style.configure(
            self.style_name,
            font=("Helvetica", 160),
            foreground="black",
            height=16,
            background="SteelBlue2",
        )
        self._cell = ttk.Button(text=value)
        self._cell.grid(row=row + 2, column=column)
        # command binding
        self._cell.bind("<1>", self.on_click)
        self._cell.bind("<Enter>", self.on_enter)
        self._cell.bind("<Leave>", self.on_leave)

    def __len__(self) -> int:
        """Changes Cell's __len__ method for calculating lengths in Board.delete_cell method"""
        return len(self._value)

    def on_enter(self, event):
        self.style.configure(self.style_name, foreground="yellow")
        self._root.update()
        # event.widget.config(foreground="yellow")

    def on_leave(self, event):
        self.style.configure(self.style_name, foreground="white")
        self._root.update()
        # event.widget.config(foreground="white")

    def on_click(self, event: tki.Event):
        """
        Handles cell clicks.
        If cell is good to click, changes cell to be inactive
        Otherwise sends an error message
        """
        valid_press = self.validate_press(self)
        if (not self._is_pressed) and valid_press:
            self._is_pressed = not self._is_pressed
            cell_activity = self.get_cell_new_activity()
            self._cell.configure(state=cell_activity)
            self.add_to_curr_word(self._value, (self.row, self.column))
            self.set_label("Nice Pick!", "green")
        else:
            self.set_label("Invalid Pick", "red")

    def get_cell_new_activity(self) -> str:
        """
        Helper method for on_click.
        Returns tki state according to is_pressed.
        """
        if self._is_pressed:
            return tki.DISABLED
        else:
            return tki.NORMAL

    def reset(self):
        """Resets cell activity"""
        self._is_pressed = False
        self._cell.configure(state=tki.NORMAL)
