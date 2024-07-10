import tkinter as tk
from tkinter import messagebox
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator
from BrailleKeyboard import BrailleKeyboard

class BrailleApp:
    def __init__(self, root, translator, image_generator):
        self.root = root
        self.translator = translator
        self.image_generator = image_generator
        self.root.title("Transcriptor Braille")

        # Configurar modo maximizado
        self.root.state('zoomed')

        fuente_grande = ('Helvetica', 14)

        # Entradas y etiquetas
        self.label_esp = tk.Label(root, text="Texto en Español:", font=fuente_grande)
        self.label_esp.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.text_esp = tk.Text(root, height=10, width=50, font=fuente_grande)
        self.text_esp.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.label_brl = tk.Label(root, text="Texto en Braille:", font=fuente_grande)
        self.label_brl.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.text_brl = tk.Text(root, height=10, width=50, font=fuente_grande)
        self.text_brl.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        # Botones
        self.btn_esp_to_brl = tk.Button(root, text="Español a Braille", command=self.convertir_esp_a_brl, font=fuente_grande)
        self.btn_esp_to_brl.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        self.btn_brl_to_esp = tk.Button(root, text="Braille a Español", command=self.convertir_brl_a_esp, font=fuente_grande)
        self.btn_brl_to_esp.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        self.btn_teclado_virtual = tk.Button(root, text="Teclado en Braile", command=self.teclado_virtual, font=fuente_grande)
        self.btn_teclado_virtual.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

        self.btn_imprimir_espejo = tk.Button(root, text="Imprimir en Espejo", command=self.imprimir_espejo, font=fuente_grande)
        self.btn_imprimir_espejo.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        # Botones de copiar
        self.btn_copiar_esp = tk.Button(root, text="Copiar Texto Español", command=self.copiar_texto_esp, font=fuente_grande)
        self.btn_copiar_esp.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

        self.btn_copiar_brl = tk.Button(root, text="Copiar Texto Braille", command=self.copiar_texto_brl, font=fuente_grande)
        self.btn_copiar_brl.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

        # Configurar el ajuste de columnas y filas
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def convertir_esp_a_brl(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl = self.translator.texto_a_braille(texto_esp)
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl)

    def convertir_brl_a_esp(self):
        texto_brl = self.text_brl.get("1.0", tk.END).strip()
        texto_esp = self.translator.braille_a_texto(texto_brl)
        self.text_esp.delete("1.0", tk.END)
        self.text_esp.insert(tk.END, texto_esp)

    def teclado_virtual(self):
        self.teclado_window = tk.Toplevel(self.root)
        self.teclado_window.title("Teclado de Braille")
        self.teclado = BrailleKeyboard(self.teclado_window, self.on_braille_input)
        self.teclado_window.mainloop()

    def on_braille_input(self, braille_text):
        current_text = self.text_brl.get("1.0", tk.END).strip()
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, current_text + braille_text)

    def generar_senaletica(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        nombre_archivo = "senaletica.png"
        self.image_generator.generar_senaletica_braille(texto_esp, nombre_archivo)
        messagebox.showinfo("Generación de Señalética", f"Señalética Braille guardada como {nombre_archivo}")

    def imprimir_espejo(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()
        texto_brl_espejo = self.image_generator.imprimir_en_espejo_braille(texto_esp)
    
        # Actualizar la pantalla de texto en Braille con el texto invertido
        self.text_brl.delete("1.0", tk.END)
        self.text_brl.insert(tk.END, texto_brl_espejo)
    
        # Generar y guardar la imagen con el texto invertido en Braille
        nombre_archivo = "espejo.png"  # Nombre del archivo para la imagen en espejo
        self.image_generator.generar_senaletica_braille(texto_brl_espejo, nombre_archivo)
    
        # Mostrar mensaje de confirmación
        messagebox.showinfo("Generación de Imagen en Espejo", f"Imagen en espejo guardada como {nombre_archivo}")

    def copiar_texto_esp(self):
        texto_esp = self.text_esp.get("1.0", tk.END).strip()

        # Copiar texto en español al portapapeles
        self.root.clipboard_clear()
        self.root.clipboard_append(texto_esp)
        self.root.update()

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Copiar Texto", "Texto copiado al portapapeles con éxito.")

    def copiar_texto_brl(self):
        texto_brl = self.text_brl.get("1.0", tk.END).strip()

        # Copiar texto en Braille al portapapeles
        self.root.clipboard_clear()
        self.root.clipboard_append(texto_brl)
        self.root.update()

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Copiar Texto", "Texto copiado al portapapeles con éxito.")
