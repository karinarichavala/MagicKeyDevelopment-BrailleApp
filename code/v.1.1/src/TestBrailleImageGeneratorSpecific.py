import unittest
from unittest.mock import patch, MagicMock
from PIL import Image, ImageChops
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator

class TestBrailleImageGenerator(unittest.TestCase):

    @patch('tkinter.filedialog.asksaveasfilename', return_value='test_output.png')
    @patch('PIL.Image.Image.save')
    def test_guardar_senaletica_generada(self, mock_save, mock_asksaveasfilename):
        # Configurar el traductor y generador de imágenes
        translator = BrailleTranslator('brailleDictionary.txt')
        generator = BrailleImageGenerator(translator)

        # Texto de prueba
        texto = "Peligro"

        # Llamar al método de generación de señalética
        generator.generar_senaletica_braille(texto, 'test_output.png')

        # Verificar que la ruta del archivo guardado es la esperada
        mock_asksaveasfilename.assert_called_once()
        self.assertEqual(mock_asksaveasfilename.return_value, 'test_output.png')

        # Verificar que el método save de PIL.Image fue llamado correctamente
        mock_save.assert_called_once_with('test_output.png')

    @patch('tkinter.filedialog.asksaveasfilename', return_value='test_output.png')
    @patch('PIL.Image.Image.save')
    def test_verificar_contenido_imagen_generada(self, mock_save, mock_asksaveasfilename):
        # Configurar el traductor y generador de imágenes
        translator = BrailleTranslator('brailleDictionary.txt')
        generator = BrailleImageGenerator(translator)

        # Texto de prueba
        texto = "Hola"

        # Llamar al método de generación de señalética en espejo
        generator.imprimir_en_espejo_braille(texto)

        # Verificar que la ruta del archivo guardado es la esperada
        mock_asksaveasfilename.assert_called_once()
        self.assertEqual(mock_asksaveasfilename.return_value, 'test_output.png')

        # Verificar que el método save de PIL.Image fue llamado correctamente
        mock_save.assert_called_once_with('test_output.png')

        # Verificar el contenido de la imagen generada
        imagen_generada = mock_save.call_args[0][0]  # La imagen que se pasa al método save
        imagen_esperada = self.crear_imagen_esperada('⠨⠓⠕⠇⠁')

        # Comprobar si la imagen generada es la esperada
        diferencia = ImageChops.difference(imagen_generada, imagen_esperada)
        self.assertFalse(diferencia.getbbox(), "La imagen generada no es la esperada")

    def crear_imagen_esperada(self, texto_braille):
        """
        Crear una imagen de prueba con el texto Braille esperado.
        """
        img = Image.new('RGB', (len(texto_braille) * 30, 50), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype('Font/ONCE_CBE_6.ttf', 30)
        d.text((10, 10), texto_braille, font=font, fill=(0, 0, 0))
        return img

if __name__ == '__main__':
    unittest.main()
