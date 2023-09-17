# def on_click(e):
#     print("hi")
#     # print(e.value)
import tkinter as tki
import tkinter.ttk as ttk

# style = ttk.Style()
# style.configure("TButton", fg="red", bg = "blue" )

button_styles = {
    # "relief": tki.SUNKEN,
    "padx": "10",
    "pady": "10",
    # "bg": "red",
    # "fg": "red"
    # "cursor": "man"
}

selected_button_Styles = {"curser": "X_cursor"}

input_styles = {
    # "fg": "black",
    # "disabledforeground": "white",
    # "pady": 10,
    # "bg": "black",
    # "underline": 0
}

# def on_click(event):
#     print(event, self._value, "hi")
#     button_activity = self.set_is_pressed()
#     print(self._is_pressed)
#     self._button.configure(state=button_activity)
#     return self._value


def set_is_pressed(self):
    self._is_pressed = not self._is_pressed
    if self._is_pressed:
        return tki.DISABLED
    else:
        return tki.NORMAL
