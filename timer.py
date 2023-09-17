import tkinter as tki
import tkinter.ttk as ttk


class Timer:
    def __init__(self, root, on_game_end):
        self._root = root
        self.on_game_end = on_game_end
        self.time = 3 * 60 * 1000
        # self.time = 3 * 1000 # for testing
        self.time_var = tki.StringVar(self._root, value=self.format_time())
        # self.time_int = tki.IntVar(value=3 * 60 * 1000)
        self.time_label = ttk.Label(textvariable=self.time_var)
        self.time_label.grid(row=1, column=0)

    def update_time(self):
        if self.time >= 0:
            self.time_var.set(self.format_time())
            self.time -= 1000
            self._root.after(1000, self.update_time)
        elif self.time < 0:
            self.on_game_end()
            # pass
            # print("hi")

    def restart_timer(self):
        self.time = 3 * 60 * 1000
        # self.time_var.set(self.format_time())
        self.update_time()

    def format_time(self):
        minutes, seconds = divmod(self.time // 1000, 60)
        return f"{minutes:02}:{seconds:02}"
