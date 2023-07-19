import tkinter as tk
from tkinter import messagebox


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("348x410")  # Set the window size here

        self.result = ""
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Consolas", 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("+", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("-", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("*", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("/", 4, 3),
            ("C", 5, 0),
        ]

        for text, row, col in buttons:
            button = tk.Button(self, text=text, width=5, height=2, font=("Consolas", 14))
            button.grid(row=row, column=col, padx=5, pady=5)
            button.config(command=lambda btn=button: self.handle_button_click(btn))

        equal_button = tk.Button(self, text="=", width=5, height=2, font=("Consolas", 14))
        equal_button.grid(row=4, column=2, columnspan=1, padx=2, pady=5)
        equal_button.config(command=lambda btn=equal_button: self.handle_button_click(btn))

    def handle_button_click(self, button):
        button_text = button["text"]
        if button_text == "=":
            self.calculate()
        elif button_text == "C":
            self.clear()
        else:
            self.result += button_text
            self.update_entry()

    def calculate(self):
        try:
            result = eval(self.result)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.result = str(result)
        except ZeroDivisionError:
            messagebox.showwarning("Error", "Cannot divide by zero. What the heck bro?")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.clear()
        finally:
            self.update_entry()

    def clear(self):
        self.result = ""
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.result)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()