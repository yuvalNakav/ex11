import tkinter
import tkinter as tki
# from tkinter import ttk
import gui_helpers as helper
import tkinter.ttk as ttk
import boggle_logics as logics


class Cell:
    def __init__(self, value, row, column, root, add_to_curr_word, validate_press):
        self._root = root
        self._value = value
        self.row = row
        self.column = column

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 18), foreground="black", highlightcolor="blue", height=8,
                             highlightthickness=5, bordercolor="green", focuscolor="green",
                             activebackground="black", disabledbackground="green")
        self._is_pressed = False
        self.add_to_curr_word = add_to_curr_word
        self.change_curr_cell = validate_press
        style = ttk.Style()
        self._cell = ttk.Button(text=value)
        self._cell.grid(row=row + 2, column=column)
        self._cell.bind("<1>", self.on_click)
        self._cell.bind("<Enter>", self.on_enter)
        self._cell.bind("<Leave>", self.on_leave)

    def on_click(self, event):
        valid_press = self.change_curr_cell(self)
        if (not self._is_pressed) and valid_press:
            cell_activity = self.set_is_pressed()
            # print(self._is_pressed)
            self._cell.configure(state=cell_activity)
            self.add_to_curr_word(self._value, (self.row, self.column))

    def on_enter(self, event):
        # print("hiu")
        self.style.configure("Parent.TButton", foreground="lightcoral")  # Change the background color on hover

    def on_leave(self, event):
        # print("bye")
        self.style.configure("Parent.TButton", foreground="lightblue")  # Restore the background color

    def set_is_pressed(self):
        self._is_pressed = not self._is_pressed
        if self._is_pressed:
            return tki.DISABLED
        else:
            return tki.NORMAL

    def restart(self):
        self._is_pressed = False
        self._cell.configure(state=tki.NORMAL)

