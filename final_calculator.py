import tkinter as tk
import math

bg_for_labels = "#212f3d"
fg_for_labels = "#f4f6f7"

button_color = "#34495e"
button_color2 = "#5d6d7e"
button_color3 = "#2e4053"


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("350x600")
        self.window.resizable(True, True)
        self.window.title("Calculator")

        self.display_frame = self.create_display_frame()

        self.history_text = ""
        self.current_text = ""

        self.display_history_label = self.create_history_label(self.history_text)
        self.display_current_label = self.create_current_label(self.current_text)

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 3)
        }

        self.operations = {
            "+": "+",
            "-": "-",
            "*": "\u00D7",
            "/": "\u00F7",
        }

        self.display_buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operation_buttons()
        self.clear_button()
        self.positive_negative_button()
        self.square_button()
        self.square_root_button()
        self.equals_button()

        self.display_buttons_frame.rowconfigure(0, weight=1)

        for i in range(1, 5):
            self.display_buttons_frame.rowconfigure(i, weight=1)
            self.display_buttons_frame.columnconfigure(i, weight=1)

    # ==================creating frames for buttons and result====================
    def create_display_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window, height=350)
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)
        return frame

    # ==================labels for the results=====================================
    def create_history_label(self, history_text):
        label = tk.Label(self.display_frame, text=history_text, font="arial 15", bg=bg_for_labels, fg=fg_for_labels,
                         anchor=tk.SE)
        label.pack(expand=True, fill="both")
        return label

    def create_current_label(self, current_text):
        label = tk.Label(self.display_frame, text=current_text, font="arial 27", bg=bg_for_labels, fg=fg_for_labels,
                         anchor=tk.E)
        label.pack(expand=True, fill="both")
        return label

    # =================updating labels with the result===========================
    def update_history_label(self):
        expression = self.history_text

        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')

        self.display_history_label.config(text=expression)

    def update_current_label(self):
        self.display_current_label.config(text=self.current_text[:21])

    def add_to_expresion(self, value):
        self.current_text += str(value)
        self.update_current_label()

    # ======================clear button and the functionallity=================
    def clear_button(self):
        button = tk.Button(self.display_buttons_frame, text="C", bg=button_color2, fg=fg_for_labels, font="Arial 20",
                           bd=3,
                           command=self.clear_button_functionality)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def clear_button_functionality(self):
        self.current_text = ""
        self.history_text = ""
        self.update_history_label()
        self.update_current_label()

    # ======================square button and the functionallity=================
    def square_button(self):
        button = tk.Button(self.display_buttons_frame, text="x\u00B2", bg=button_color2, fg=fg_for_labels, bd=3,
                           font="Arial 20", command=self.square_button_functionallity)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square_button_functionallity(self):
        current = self.current_text
        for k in self.operations.keys():
            if k in self.history_text:
                self.history_text += f'sqr({eval(current) ** 2})'
                self.current_text = ""
                break
        else:
            self.history_text = f'sqr({current})'
            self.current_text = f'{eval(current) ** 2}'
        self.update_history_label()
        self.update_current_label()

    # ======================square root button and the functionallity=================
    def square_root_button(self):
        button = tk.Button(self.display_buttons_frame, text="\u00B2\u221Ax", bg=button_color2, fg=fg_for_labels, bd=3,
                           font="Arial 20", command=self.square_root_button_functionallity)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def square_root_button_functionallity(self):
        current = self.current_text
        for k in self.operations.keys():
            if k in self.history_text:
                self.history_text += f'sqrt({math.sqrt(eval(current))})'
                self.current_text = ""
                break
        else:
            self.history_text = f'sqrt({current})'
            self.current_text = f'{math.sqrt(eval(current))}'
        self.update_history_label()
        self.update_current_label()

    # ======================equals button and the functionallity=================
    def equals_button(self):
        button = tk.Button(self.display_buttons_frame, text="=", font="Arial 20", bd=3,
                           bg=button_color2, fg=fg_for_labels, command=self.equals_button_functionality)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def equals_button_functionality(self):
        text = self.history_text
        if "sqrt" in self.history_text and "sqr" in self.history_text:
            self.history_text = text.replace("sqrt", "").replace("(", "").replace(")", "").replace("sqr", "")
        if "sqrt" in self.history_text:
            self.history_text = text.replace("sqrt", "").replace("(", "").replace(")", "")
        if "sqr" in self.history_text:
            self.history_text = text.replace("sqr", "").replace("(", "").replace(")", "")
        try:
            self.history_text += self.current_text
            self.update_history_label()
            self.current_text = str(eval(self.history_text))
        except ZeroDivisionError:
            self.current_text = "Cannot divide by zero"
        except:
            self.current_text = "An error occurred."
        finally:
            self.update_current_label()

    # ======================positvie/negative button and the functionallity=================
    def positive_negative_button(self):
        button = tk.Button(self.display_buttons_frame, text="+/-", bg=button_color, fg=fg_for_labels, font="Arial 20",
                           bd=3,
                           command=self.positive_negative_button_functionallity)
        button.grid(row=4, column=1, sticky=tk.NSEW)

    def positive_negative_button_functionallity(self):
        if "-" not in self.current_text and self.current_text != "":
            self.current_text = '-' + self.current_text
        else:
            self.current_text = self.current_text.replace("-", "")
        self.update_current_label()

    # ======================creating the digit/operations buttons and their functionallities=================
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.display_buttons_frame, text=str(digit), bg=button_color, fg=fg_for_labels, bd=3,
                               font="Arial 20", command=lambda x=digit: self.add_to_expresion(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operation_buttons(self):
        i = 0
        for operation, symbol in self.operations.items():
            button = tk.Button(self.display_buttons_frame, text=symbol, bg=button_color3, fg=fg_for_labels, bd=3,
                               font="Arial 20", command=lambda x=operation: self.append_operation(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    # ======================appending the operation and the number to the history label=================
    def append_operation(self, operation):
        if "sqrt" in self.history_text:
            self.history_text.replace("sqrt", "").replace("(", "").replace(")", "")
            if "+" not in self.history_text and "-" not in self.history_text and "*" not in self.history_text \
                    and "/" not in self.history_text:
                self.history_text = ""
                self.update_history_label()

        if "sqr" in self.history_text:
            self.history_text.replace("sqr", "").replace("(", "").replace(")", "")
            if "+" not in self.history_text and "-" not in self.history_text and "*" not in self.history_text \
                    and "/" not in self.history_text:
                self.history_text = ""
                self.update_history_label()

        self.current_text += operation
        self.history_text += self.current_text
        self.current_text = ""
        self.update_history_label()
        self.update_current_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
