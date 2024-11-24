from selenium.webdriver.common.by import By

class MapsObject:
    # Registro
    btnRegistro = (By.LINK_TEXT, "Sign up")
    txtNombre = (By.ID, "full-name")
    txtCorreo = (By.ID, "email")
    txtContrasena = (By.CSS_SELECTOR, 'input.input.input-bordered[type="password"]')
    txtConfirmarContrasena = (By.CSS_SELECTOR, 'input.input.input-bordered[type="password"][id="confirm-password"]')
    btnRegistarse = (By.CSS_SELECTOR, 'button[type="submit"]')
    validarRegistro = (By.XPATH, '//div[contains(text(), "Successful registration!")]')
    

    # Login
    txtCorreoLogin = (By.ID, "email")
    txtContrasenaLogin = (By.CSS_SELECTOR, 'input.input.input-bordered[type="password"][id="password"]')
    btnLogin = (By.XPATH, '//button[contains(text(), "Sign in")]')
    txtNombreMenu = (By.XPATH, '//h2[@class="font-bold"]')
    btnMenu = (By.XPATH, '//label[@class="btn btn-ghost btn-circle avatar"]')
    btnCerrarSesion = (By.XPATH, '//a[text()="Logout"]')
