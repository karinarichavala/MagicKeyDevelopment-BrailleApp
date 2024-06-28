import tkinter as tk
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator
from BrailleApp import BrailleApp

if __name__ == "__main__":
    dict_file = 'brailleDictionary.txt'
    translator = BrailleTranslator(dict_file)
    image_generator = BrailleImageGenerator(translator)
    root = tk.Tk()
    app = BrailleApp(root, translator, image_generator)
    root.mainloop()
                