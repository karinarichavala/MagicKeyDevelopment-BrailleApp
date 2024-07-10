import unittest
from BrailleTranslator import BrailleTranslator

class TestBrailleToTextoTranslator(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del traductor con el diccionario proporcionado
        self.translator = BrailleTranslator('brailleDictionary.txt')

    def test_abecedario_braille_minusculas(self):
        # Caso de prueba 1: Abecedario braille en minúsculas
        texto = '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
        esperado = 'abcdefghijklmnopqrstuvwxyz'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_abecedario_braille_mayusculas(self):
        # Caso de prueba 2: Abecedario braille en mayúsculas
        texto = '⠨⠁⠨⠃⠨⠉⠨⠙⠨⠑⠨⠋⠨⠛⠨⠓⠨⠊⠨⠚⠨⠅⠨⠇⠨⠍⠨⠝⠨⠕⠨⠏⠨⠟⠨⠗⠨⠎⠨⠞⠨⠥⠨⠧⠨⠺⠨⠭⠨⠽⠨⠵'
        esperado = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)
    
    def test_vocales_acentuadas_braille(self):
        # Caso de prueba 3: Vocales acentuadas en braille
        texto = '⠷⠮⠌⠬⠾'
        esperado = 'áéíóú'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_letras_especiales_braille(self):
        # Caso de prueba 4: Letras especiales en braille (ñ y ü)
        texto = '⠻⠳'
        esperado = 'ñü'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_signos_basicos_braille(self):
        # Caso de prueba 5: Signos básicos en braille
        texto = '⠄⠂⠆⠒⠤⠦⠖⠢⠣⠜⠖⠔⠶⠲⠤'
        esperado = '.,;:_“”¡!¿?()+*=÷-'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_numeros_una_cifra_braille(self):
        # Caso de prueba 6: Números de una cifra en braille
        textos = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
        esperados = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for texto, esperado in zip(textos, esperados):
            resultado = self.translator.braille_a_texto(texto)
            self.assertEqual(resultado, esperado)

    def test_numeros_dos_cifras_braille(self):
        # Caso de prueba 7: Números de dos cifras en braille
        texto = '⠼⠁⠃'
        esperado = '12'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_numeros_punto_decimal_braille(self):
        # Caso de prueba 8: Números con punto decimal en braille
        texto = '⠼⠁⠄⠃'
        esperado = '1.2'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

    def test_numeros_coma_decimal_braille(self):
        # Caso de prueba 9: Números con coma decimal en braille
        texto = '⠼⠃⠂⠉'
        esperado = '2,3'
        resultado = self.translator.braille_a_texto(texto)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
