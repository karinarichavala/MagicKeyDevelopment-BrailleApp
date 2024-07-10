import unittest
import psutil
import time
from BrailleTranslator import BrailleTranslator
from BrailleImageGenerator import BrailleImageGenerator

class TestApplicationResourceUsage(unittest.TestCase):
    def setUp(self):
        # Inicializar el traductor y el generador de imágenes
        self.translator = BrailleTranslator('brailleDictionary.txt')
        self.generator = BrailleImageGenerator(self.translator)

    def monitor_resources(self, duration=10):
        # Monitorear el uso de recursos durante un periodo de tiempo
        cpu_usage = []
        memory_usage = []
        for _ in range(duration):
            cpu_usage.append(psutil.cpu_percent(interval=1))
            memory_usage.append(psutil.virtual_memory().percent)
        return cpu_usage, memory_usage

    def test_resource_usage_windows_10(self):
        # Entorno de prueba 1: Windows 10 con Chrome, Word y Spotify en ejecución
        print("Iniciando prueba en Windows 10 con Chrome, Word y Spotify...")
        cpu_usage, memory_usage = self.monitor_resources()
        print(f"Uso de CPU: {cpu_usage}")
        print(f"Uso de Memoria: {memory_usage}")

    def test_resource_usage_macos_catalina(self):
        # Entorno de prueba 2: macOS Catalina con Safari, Pages e iTunes en ejecución
        print("Iniciando prueba en macOS Catalina con Safari, Pages e iTunes...")
        cpu_usage, memory_usage = self.monitor_resources()
        print(f"Uso de CPU: {cpu_usage}")
        print(f"Uso de Memoria: {memory_usage}")

    def test_resource_usage_windows_11(self):
        # Entorno de prueba 3: Windows 11 con Fornite, VLC Media Player y Photoshop en ejecución
        print("Iniciando prueba en Windows 11 con Fornite, VLC Media Player y Photoshop...")
        cpu_usage, memory_usage = self.monitor_resources()
        print(f"Uso de CPU: {cpu_usage}")
        print(f"Uso de Memoria: {memory_usage}")

if __name__ == '__main__':
    unittest.main()
