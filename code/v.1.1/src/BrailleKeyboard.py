import tkinter as tk

class BrailleKeyboard(tk.Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.title("Teclado de Braille")
        self.geometry("1100x800")
        self.create_buttons()


    def create_buttons(self):
        braille_dict = {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
            'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
            'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', 'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠬',
            'ú': '⠾', 'ü': '⠳', 'ñ': '⠻', '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
            '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '¡': '⠖', '!': '⠖',
            '¿': '⠦', '?': '⠦', '#': '⠼', '*': '⠔', '(': '⠐⠣', ')': '⠐⠜', '$': '⠈⠎', '%': '⠨⠴', '&': '⠈⠯', '-': '⠤',
            '_': '⠠⠤', '+': '⠐⠖', '=': '⠨⠿', '/': '⠌', '\\': '⠡', '"': '⠘⠶', "'": '⠄', '`': '⠈⠜', '^': '⠘⠔',
            '|': '⠸⠶', '~': '⠈⠱', '<': '⠦', '>': '⠴', '@': '⠈⠁', 'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙',
            'E': '⠠⠑', 'F': '⠠⠋', 'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇',
            'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗', 'S': '⠠⠎', 'T': '⠠⠞',
            'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭', 'Y': '⠠⠽', 'Z': '⠠⠵', 'Á': '⠠⠷', 'É': '⠠⠮',
            'Í': '⠠⠌', 'Ó': '⠠⠬', 'Ú': '⠠⠾', 'Ü': '⠠⠳', 'Ñ': '⠠⠻'
        }

        row, col = 0, 0
        max_columns = 15

        for key, value in braille_dict.items():
            btn = tk.Button(self, text=f"{key}\n{value}", command=lambda value=value: self.on_button_click(value))
            btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
            col += 1
            if col >= max_columns:
                col = 0
                row += 1

    def on_button_click(self, value):
        self.callback(value)
