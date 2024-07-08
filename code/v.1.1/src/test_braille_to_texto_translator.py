import unittest
from BrailleTranslator import BrailleTranslator

class TestBrailleToTextoTranslator(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del traductor con el diccionario proporcionado
        self.translator = BrailleTranslator('brailleDictionary.txt')

    def test_abecedario_braille_minusculas(self):
        # Caso de prueba 10: Abecedario braille en minúsculas
        texto = '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
        esperado = 'abcdefghijklmnopqrstuvwxyz'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_abecedario_braille_mayusculas(self):
        # Caso de prueba 11: Abecedario braille en mayúsculas
        texto = '⠨⠁⠨⠃⠨⠉⠨⠙⠨⠑⠨⠋⠨⠛⠨⠓⠨⠊⠨⠚⠨⠅⠨⠇⠨⠍⠨⠝⠨⠕⠨⠏⠨⠟⠨⠗⠨⠎⠨⠞⠨⠥⠨⠧⠨⠺⠨⠭⠨⠽⠨⠵'
        esperado = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)
    
    def test_vocales_acentuadas_braille(self):
        # Caso de prueba 12: Vocales acentuadas en braille
        texto = '⠷⠮⠌⠬⠾⠳'
        esperado = 'áéíóúü'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)


    def test_signos_basicos_braille(self):
        # Caso de prueba 13: Signos básicos en braille
        texto = '⠂⠄⠆⠒⠖⠢⠢'
        esperado = ',.;:!?¿'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
