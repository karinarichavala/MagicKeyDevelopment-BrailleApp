class BrailleTranslator:
    def __init__(self, dict_file):
        self.braille_dict = self.load_dictionary(dict_file)
        self.num_indicator = '⠼'
        self.decimal_point = '⠨'
        self.decimal_comma = '⠐'

    def load_dictionary(self, dict_file):
        braille_dict = {}
        with open(dict_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if ':' in line:
                    char, braille = line.split(':', 1)
                    braille_dict[char] = braille
                else:
                    # Manejar líneas con formato incorrecto
                    pass
        return braille_dict

    def texto_a_braille(self, texto):
        braille_texto = ''
        numero = False  # Usamos una bandera para saber si estamos en un número
        for char in texto:
            if char.isdigit() or char == ',' or char == '.':
                if not numero:
                    braille_texto += self.num_indicator
                    numero = True
                if char == '.':
                    braille_texto += self.decimal_point
                elif char == ',':
                    braille_texto += self.decimal_comma
                else:
                    braille_texto += self.braille_dict.get(char, '')
            else:
                if numero:
                    numero = False  # Reseteamos el estado de número
                braille_texto += self.braille_dict.get(char, char)
        return braille_texto

    def braille_a_texto(self, braille_texto):
        texto = ''
        numero = False  # Usamos una bandera para saber si estamos en un número
        i = 0
        while i < len(braille_texto):
            char = braille_texto[i]
            if char == self.num_indicator:
                numero = True
                i += 1
                continue
            if numero:
                if char == self.decimal_point:
                    texto += '.'
                elif char == self.decimal_comma:
                    texto += ','
                else:
                    num_char = next((key for key, value in self.braille_dict.items() if value == char), None)
                    if num_char is not None:
                        texto += num_char
                    else:
                        numero = False  # Reseteamos el estado de número
                        texto += char
                i += 1
                continue

            if i < len(braille_texto) - 1:
                double_char = braille_texto[i:i + 2]
                texto_char = next((key for key, value in self.braille_dict.items() if value == double_char), None)
                if texto_char:
                    texto += texto_char
                    i += 2
                    continue

            texto_char = next((key for key, value in self.braille_dict.items() if value == char), None)
            texto += texto_char if texto_char else char
            i += 1
        return texto