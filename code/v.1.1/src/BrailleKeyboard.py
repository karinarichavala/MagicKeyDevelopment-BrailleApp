import tkinter as tk
from tkinter import messagebox

class BrailleKeyboard(tk.Toplevel):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.shift_active = False  # Estado del botón Shift
        self.title("Teclado de Braille")
        
        # Obtener el tamaño de la ventana principal
        self.master.update_idletasks()
        main_width = self.master.winfo_width()
        main_height = self.master.winfo_height()
        main_x = self.master.winfo_x()
        main_y = self.master.winfo_y()

        # Establecer la posición del teclado en la parte inferior derecha
        self.geometry(f"1410x400+{main_x + main_width - 1500}+{main_y + main_height - 400}")
        
        self.create_buttons()

    def create_buttons(self):
        self.braille_dict = {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
            'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
            'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', 'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠬',
            'ú': '⠾', 'ü': '⠳', 'ñ': '⠻', '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
            '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '!': '⠖',
            '?': '⠦', '#': '⠼', '*': '⠔', '(': '⠣', ')': '⠜', '$': '⠈⠎', '%': '⠨⠴', '&': '⠈⠯', '-': '⠤',
            '_': '⠠⠤', '+': '⠐⠖', '=': '⠨⠾', '/': '⠌', '\\': '⠡', '"': '⠦', "'": '⠄', '`': '⠄', '^': '⠘⠔',
            '|': '⠸⠶', '~': '⠈⠱', '<': '⠦', '>': '⠴', '@': '⠈⠁', 'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙',
            'E': '⠠⠑', 'F': '⠠⠋', 'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇',
            'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗', 'S': '⠠⠎', 'T': '⠠⠞',
            'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭', 'Y': '⠠⠽', 'Z': '⠠⠵', 'Á': '⠠⠷', 'É': '⠠⠮',
            'Í': '⠠⠌', 'Ó': '⠠⠬', 'Ú': '⠠⠾', 'Ü': '⠠⠳', 'Ñ': '⠠⠻'
        }

        self.shift_dict = {
            '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
            '-': '_', '=': '+', '[': '{', ']': '}', '\\': '|', ';': ':', "'": '"', ',': '<', '.': '>', '/': '?',
            '`': '~'
        }

        self.qwerty_layout = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Fn', 'Win', 'Alt', 'Space', 'Alt', 'Ctrl', 'Left', 'Down', 'Up', 'Right']
        ]
        
        self.buttons = {}
        self.render_keyboard()
        
    def render_keyboard(self):
        for widget in self.winfo_children():
            widget.destroy()

        for row_index, row_keys in enumerate(self.qwerty_layout):
            for col_index, key in enumerate(row_keys):
                if key == 'Shift':
                    btn = tk.Button(self, text=key, command=self.toggle_shift)
                elif key == 'Space':
                    btn = tk.Button(self, text=key, command=lambda value=' ': self.on_button_click(value))
                else:
                    if self.shift_active and key in self.shift_dict:
                        display_key = self.shift_dict[key]
                    elif self.shift_active and key.isalpha():
                        display_key = key.upper()
                    else:
                        display_key = key

                    if display_key in self.braille_dict:
                        btn_text = f"{display_key}\n{self.braille_dict[display_key]}"
                    else:
                        btn_text = display_key

                    btn = tk.Button(self, text=btn_text, command=lambda value=display_key: self.on_button_click(value))

                btn.grid(row=row_index, column=col_index, padx=5, pady=5, ipadx=10, ipady=10)
                self.buttons[key] = btn

    def toggle_shift(self):
        self.shift_active = not self.shift_active
        self.render_keyboard()
        
    def on_button_click(self, value):
        # Llamar al callback con el valor del botón presionado
        self.callback(value)
