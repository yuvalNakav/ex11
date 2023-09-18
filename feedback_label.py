import tkinter as tki
import tkinter.ttk as ttk


class FeedbackLabel:
    """
    Feedback Label component class.
    Handles label setting
    """
    def __init__(self, root: tki.Tk, style:ttk.Style) -> None:
        self._root = root
        self.feedback = tki.StringVar()
        self.style_name = "TLabel.feedback"
        self.style = style
        self.style.configure(self.style_name, fg="Red")
        self._label = ttk.Label(textvariable=self.feedback)
        self._label.grid(row=0, column=2, columnspan=2)

    # def set_label(self, message):
    def set_label(self, message: str, color: str) -> None:
        """Sets feedback label StringVar"""
        self.feedback.set(value=message)
        self.style.configure(self.style_name, forground=color)
