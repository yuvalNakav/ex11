import tkinter as tki
import tkinter.ttk as ttk
from typing import *


class Timer:
    """
    Timer component class.
    Handles Timer functionality and location.
    """
    def __init__(self, root: tki.Tk, on_game_end: Callable):
        """
        Initializes new timer component.
        """
        self._root = root
        self.on_game_end = on_game_end
        self.time = 3 * 60 * 1000  # 3 minutes in ms
        # self.time = 3 * 1000 # for testing
        self.time_var = tki.StringVar(self._root, value=self.format_time())
        self.time_label = ttk.Label(textvariable=self.time_var)
        self.time_label.grid(row=1, column=0)

    def update_time(self) -> None:
        """Main timer method.
        Handles timer intervals."""
        if self.time >= 0:
            self.time_var.set(self.format_time())
            self.time -= 1000
            self._root.after(1000, self.update_time)
        elif self.time < 0: # time ended
            self.on_game_end()

    def restart_timer(self) -> None:
        """Resets and restart timer for 3 minutes """
        self.time = 3 * 60 * 1000
        self.update_time()

    def format_time(self) -> str:
        """formats time for displaying. Returns formatted string"""
        minutes, seconds = divmod(self.time // 1000, 60)
        return f"{minutes:02}:{seconds:02}"
