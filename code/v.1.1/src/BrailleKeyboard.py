import tkinter as tk
from tkinter import messagebox

class BrailleKeyboard(tk.Toplevel):
    def __init__(self, master, callback, text_widget):
        super().__init__(master)
        self.callback = callback
        self.text_widget = text_widget  # Guardamos la referencia del widget de texto
        self.shift_active = False  # Estado del botón Shift
        self.caps_lock_active = False  # Estado del botón Caps Lock
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
            self.grid_rowconfigure(row_index, weight=1)
            for col_index, key in enumerate(row_keys):
                self.grid_columnconfigure(col_index, weight=1)

                if key == 'Shift':
                    btn = tk.Button(self, text=key, command=self.toggle_shift)
                elif key == 'Caps Lock':
                    btn = tk.Button(self, text=key, command=self.toggle_caps_lock)
                elif key == 'Backspace':  # Aquí manejas Backspace
                    btn = tk.Button(self, text=key, command=self.on_backspace)
                elif key == 'Space':
                    btn = tk.Button(self, text=key, command=self.on_space)
                elif key == 'Enter':  # Aquí manejas Enter
                    btn = tk.Button(self, text=key, command=self.on_enter)
                else:
                    # Manejo de mayúsculas según Caps Lock y Shift
                    if self.shift_active and not self.caps_lock_active:
                        display_key = key.upper()
                    elif self.caps_lock_active and not self.shift_active:
                        display_key = key.upper()
                    elif self.caps_lock_active and self.shift_active:
                        display_key = key.lower()
                    else:
                        display_key = key.lower()

                    if display_key in self.braille_dict:
                        btn_text = f"{display_key}\n{self.braille_dict[display_key]}"
                    else:
                        btn_text = display_key

                    btn = tk.Button(self, text=btn_text, command=lambda value=display_key: self.on_button_click(value))

                btn.grid(row=row_index, column=col_index, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
                self.buttons[key] = btn

    def on_backspace(self):
        current_widget = self.text_widget

        if isinstance(current_widget, tk.Entry):
            cursor_position = current_widget.index(tk.INSERT)
            if cursor_position > 0:
                current_widget.delete(cursor_position - 1, cursor_position)

        elif isinstance(current_widget, tk.Text):
            cursor_position = current_widget.index(tk.INSERT)
            if cursor_position != "1.0":
                current_widget.delete(f"{cursor_position}-1c", cursor_position)

    def toggle_shift(self):
        self.shift_active = not self.shift_active
        self.render_keyboard()

    def toggle_caps_lock(self):
        self.caps_lock_active = not self.caps_lock_active
        self.render_keyboard()

    def on_space(self):
        self.callback(' ')

    def on_enter(self):
        self.callback('\n')

    def on_button_click(self, value):
        self.callback(value)


