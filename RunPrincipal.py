import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pag.pagObjet import PageObject
from utils.Screenshot import Screenshot
from utils.PDF import PDFUtils
import time

# Leer configuración del archivo pom.json
config_path = os.path.join(os.path.dirname(__file__), "pom/pom.json")
with open(config_path, "r") as config_file:
    config = json.load(config_file)

# Definir la URL base y el nombre del automatizador
base_url = config["base_url"]
automator_name = config["automator"]

# Inicia el driver
def iniciar_driver():
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# Caso de prueba: Registro Exitoso
def test_registro_exitoso(driver, page):
    try:
        driver.get(f"{base_url}/register")  # Construir la URL de registro

        # Navegar al registro y completar el formulario
        page.go_to_register()
        time.sleep(2)
        page.fill_registration_form("prueba aut", "prueba2@hotmail.com", "Prueba123+", "Prueba123+")
        time.sleep(2)
        page.submit_registration()

        # Validar el registro exitoso
        page.validate_error_message("Successful registration!")
        print("Caso de prueba 'Registro Exitoso' completado correctamente.")
    except Exception as e:
        print(f"Error en el caso 'Registro Exitoso': {e}")

# Caso de prueba: Login Exitoso
def test_login_exitoso(driver, page):
    try:
        driver.get(f"{base_url}/login")  # Construir la URL de login

        # Completar el formulario de login
        page.login_user("prueba2@hotmail.com", "Prueba123+")

        # Validar login exitoso
        page.validate_successful_login()

        # Cerrar sesión
        page.logout_user()
        print("Caso de prueba 'Login Exitoso' completado correctamente.")
    except Exception as e:
        print(f"Error en el caso 'Login Exitoso': {e}")

# Ejecución principal
if __name__ == "__main__":
    print("Selecciona el caso de prueba:")
    print("1. Registro Exitoso")
    print("2. Login Exitoso")
    print("3. Ejecutar todos")

    opcion = input("Selecciona una opción (1-3): ")

    # Inicializar una única instancia del driver
    driver = iniciar_driver()
    page = PageObject(driver)

    # Limpiar capturas previas y PDF
    screenshot = Screenshot(driver)
    screenshot.limpiar_screenshots()

    pdf = PDFUtils()
    pdf.limpiar_pdf()

    try:
        if opcion == "1":
            # Ejecutar registro exitoso
            test_registro_exitoso(driver, page)
        elif opcion == "2":
            # Ejecutar login exitoso
            test_login_exitoso(driver, page)
        elif opcion == "3":
            # Ejecutar todos
            test_registro_exitoso(driver, page)
            test_login_exitoso(driver, page)
        else:
            print("Opción inválida. Intenta de nuevo.")
    finally:
        # Generar PDF al finalizar
        pdf.agregar_encabezado(automator_name, base_url)
        screenshots_dir = "screenshots"
        for image_file in sorted(os.listdir(screenshots_dir)):
            if image_file.endswith(".png"):
                image_path = os.path.join(screenshots_dir, image_file)
                pdf.agregar_imagen(image_path, title=f"Captura: {image_file}")
        pdf.generar_pdf()

        # Cerrar el driver
        driver.quit()
