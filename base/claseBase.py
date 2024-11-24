from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.Screenshot import Screenshot

class claseBase:
    def __init__(self, driver):
        self.driver = driver
        self.screenshot = Screenshot(driver)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        self.screenshot.take_screenshot("click")  # Toma captura después del clic

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        self.screenshot.take_screenshot("send_keys")  # Toma captura después de enviar texto

    def clear(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
        self.screenshot.take_screenshot("clear")  # Toma captura después de limpiar el campo

    def get_text(self, locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        self.screenshot.take_screenshot("get_text")  # Toma captura después de obtener texto
        return text

    def tiempoEspera(self, segundos=0):
        time.sleep(segundos)

    def is_element_enabled(self, locator):
        """Verifica si un elemento está habilitado."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.screenshot.take_screenshot("is_element_enabled")  # Toma captura después de verificar el estado
        return element.is_enabled()
