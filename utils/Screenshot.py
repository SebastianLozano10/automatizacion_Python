import os
import time

class Screenshot:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_dir = "screenshots"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def limpiar_screenshots(self):
        """Elimina todas las capturas existentes en la carpeta de screenshots."""
        if os.path.exists(self.screenshot_dir):
            for file in os.listdir(self.screenshot_dir):
                file_path = os.path.join(self.screenshot_dir, file)
                if os.path.isfile(file_path) and file.endswith(".png"):
                    os.remove(file_path)
            print(f"Se eliminaron todas las capturas previas en '{self.screenshot_dir}'.")
        else:
            print(f"No se encontraron capturas previas en '{self.screenshot_dir}'.")

    def take_screenshot(self, action_name):
        """Toma una captura de pantalla y la guarda con un nombre específico."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Captura tomada: {screenshot_path}")
