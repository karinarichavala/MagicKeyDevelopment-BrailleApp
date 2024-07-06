import unittest
from BrailleTranslator import BrailleTranslator

class TestBrailleTranslator(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del traductor con el diccionario proporcionado
        self.translator = BrailleTranslator('brailleDictionary.txt')

    def test_abecedario_min(self):
        # Caso de prueba 1: Abecedario completo en minúsculas
        texto = 'abcdefghijklmnopqrstuvwxyz'
        esperado = '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_abecedario_may(self):
        # Caso de prueba 2: Abecedario completo en mayúsculas
        texto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        esperado = '⠠⠁⠠⠃⠠⠉⠠⠙⠠⠑⠠⠋⠠⠛⠠⠓⠠⠊⠠⠚⠠⠅⠠⠇⠠⠍⠠⠝⠠⠕⠠⠏⠠⠟⠠⠗⠠⠎⠠⠞⠠⠥⠠⠧⠠⠺⠠⠭⠠⠽⠠⠵'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_vocales_acentuadas(self):
        # Caso de prueba 3: Vocales acentuadas
        texto = 'áéíóúü'
        esperado = '⠷⠮⠌⠬⠾⠳'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_letras_especiales(self):
        # Caso de prueba 4: Letras especiales Ñ y Ü
        texto = 'ñÜ'
        esperado = '⠻⠳'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_signos_basicos(self):
        # Caso de prueba 5: Signos básicos
        texto = ',.;:!?!*+=-¡¿()'
        esperado = '⠐⠂⠆⠒⠲⠢⠖⠶⠦⠔⠐⠣⠜'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_numeros_una_cifra(self):
        # Caso de prueba 6: Números de una cifra
        texto = '0123456789'
        esperado = '⠚⠂⠆⠒⠲⠢⠖⠶⠦⠔'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_cantidades_dos_mas_cifras(self):
        # Caso de prueba 7: Cantidades de dos o más cifras
        texto = '123'
        esperado = '⠼⠁⠃⠉'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_cantidades_con_puntos(self):
        # Caso de prueba 8: Cantidades con puntos
        texto = '1.23'
        esperado = '⠼⠁⠨⠃⠉'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

    def test_cantidades_con_comas(self):
        # Caso de prueba 9: Cantidades con comas
        texto = '1,23'
        esperado = '⠼⠁⠐⠃⠉'
        resultado = self.translator.texto_a_braille(texto)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
