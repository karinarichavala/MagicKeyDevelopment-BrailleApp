from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog, messagebox

class BrailleImageGenerator:
    def __init__(self, translator):
        """
        Initializes a new instance of the class.

        Parameters:
            translator (Translator): An instance of the Translator class used for translating text to Braille.

        Returns:
            None
        """
        self.translator = translator
    
    def generar_senaletica_braille(self, texto, nombre_archivo):
        """
        Generates an image with Braille text and saves it to a file.

        This function converts a given text to its Braille equivalent, creates an image with the Braille text,
        and saves it to a specified file in png format.

        Parameters:
            texto (str): The text to be converted to Braille.
            nombre_archivo (str): The name of the file to save the Braille signage image.

        Returns:
            None
        """

        braille_text = self.translator.texto_a_braille(texto)
        nombre_archivo = filedialog.asksaveasfilename(
            defaultextension = ".*", title = "Save File", filetypes = (("PNG Files", "*.png"), ("All Files", "*.*"), ))
        img = Image.new('RGB', (len(braille_text) * 30, 50), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('Font/ONCE_CBE_6.ttf', 30)
        d.text((10, 10), braille_text, font=font, fill=(0, 0, 0))
        img.save(nombre_archivo)

    def imprimir_en_espejo_braille(self, texto):
        """
        Generates a Braille representation of the given text by looking up each character in the braille_dict and returns
        it in reverse order.

        Parameters:
            texto (str): The text to be converted to Braille.

        Returns:
            str: The Braille representation of the input text in reverse order.
        """
        braille_text = self.translator.texto_a_braille(texto)
        return braille_text[::-1]
