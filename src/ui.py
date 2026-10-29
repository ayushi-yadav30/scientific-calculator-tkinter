import customtkinter as ctk
from calculator_logic import calculate

# ---------- Colors (appearance control) ----------
BODY_COLOR = "#4F7CAC"        # calculator body (steel blue)
DISPLAY_BG = "#F3EFC9"        # cream LCD screen
DISPLAY_TEXT = "#E8892B"      # orange digits

NUMBER_BG = "#F4F6F8"         # number buttons
NUMBER_HOVER = "#DDE3EA"
NUMBER_TEXT = "#2C3E50"

OPERATOR_BG = "#C5D3E2"       # + - * /
OPERATOR_HOVER = "#AFC0D3"

CLEAR_BG = "#F5C542"          # C button (yellow)
CLEAR_HOVER = "#E0B030"

BACKSPACE_BG = "#E8A598"      # backspace
BACKSPACE_HOVER = "#D98E80"

EQUAL_BG = "#2F6DB5"          # = button
EQUAL_HOVER = "#255A99"


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Basic Calculator")
        self.geometry("340x540")
        self.configure(fg_color=BODY_COLOR)

        ctk.set_appearance_mode("light")

        # Display box
        self.display = ctk.CTkEntry(
            self,
            font=("Consolas", 34, "bold"),
            justify="right",
            height=80,
            corner_radius=10,
            border_width=0,
            fg_color=DISPLAY_BG,
            text_color=DISPLAY_TEXT,
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=(25, 15), sticky="nsew")
        self.display.configure(state="disabled")

        # Buttons: (label, row, column)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
            (".", 5, 0), ("⌫", 5, 1),
        ]

        for (text, row, col) in buttons:
            style = self.get_button_style(text)
            button = ctk.CTkButton(
                self,
                text=text,
                font=("Arial", 22, "bold"),
                height=60,
                corner_radius=12,
                fg_color=style["bg"],
                hover_color=style["hover"],
                text_color=style["text"],
                command=lambda t=text: self.on_button_click(t),
            )
            button.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

        # Grid resizing
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

        # Keyboard input
        self.bind("<Key>", self.on_key_press)

    # ---------- Button styling ----------
    def get_button_style(self, text):
        if text in "+-*/":
            return {"bg": OPERATOR_BG, "hover": OPERATOR_HOVER, "text": NUMBER_TEXT}
        elif text == "C":
            return {"bg": CLEAR_BG, "hover": CLEAR_HOVER, "text": NUMBER_TEXT}
        elif text == "⌫":
            return {"bg": BACKSPACE_BG, "hover": BACKSPACE_HOVER, "text": NUMBER_TEXT}
        elif text == "=":
            return {"bg": EQUAL_BG, "hover": EQUAL_HOVER, "text": "white"}
        else:  # numbers and "."
            return {"bg": NUMBER_BG, "hover": NUMBER_HOVER, "text": NUMBER_TEXT}

    # ---------- Display helpers ----------
    def set_display(self, text):
        self.display.configure(state="normal")
        self.display.delete(0, ctk.END)
        self.display.insert(0, text)
        self.display.configure(state="disabled")

    def get_display(self):
        return self.display.get()

    # ---------- Actions ----------
    def append_value(self, value):
        current = self.get_display()
        if current == "Error":
            current = ""
        self.set_display(current + value)

    def clear(self):
        self.set_display("")

    def backspace(self):
        current = self.get_display()
        if current == "Error":
            self.clear()
        else:
            self.set_display(current[:-1])

    def evaluate(self):
        expression = self.get_display()
        if expression == "":
            return
        self.set_display(calculate(expression))

    # ---------- Event handlers ----------
    def on_button_click(self, value):
        if value == "C":
            self.clear()
        elif value == "⌫":
            self.backspace()
        elif value == "=":
            self.evaluate()
        else:
            self.append_value(value)

    def on_key_press(self, event):
        if event.char != "" and event.char in "0123456789+-*/.":
            self.append_value(event.char)
        elif event.keysym in ("Return", "KP_Enter"):
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.keysym == "Escape" or event.char in ("c", "C"):
            self.clear()