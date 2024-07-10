import unittest
from unittest.mock import patch, MagicMock
from PIL import Image

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

if __name__ == '__main__':
    unittest.main()

