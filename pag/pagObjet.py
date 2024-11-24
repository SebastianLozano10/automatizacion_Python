from base.claseBase import claseBase
from maps.mapObjet import MapsObject

class PageObject(claseBase):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_register(self):
        """Realiza clic en el botón de registro."""
        self.click(MapsObject.btnRegistro)
        self.tiempoEspera(2)

    def fill_registration_form(self, name, email, password, confirm_password):
        """Llena el formulario de registro."""
        self.send_keys(MapsObject.txtNombre, name)
        self.tiempoEspera(2)
        self.send_keys(MapsObject.txtCorreo, email)
        self.tiempoEspera(2)
        self.send_keys(MapsObject.txtContrasena, password)
        self.tiempoEspera(2)
        self.send_keys(MapsObject.txtConfirmarContrasena, confirm_password)
        self.tiempoEspera(2)

    def submit_registration(self):
        """Hace clic en el botón de registro."""
        self.click(MapsObject.btnRegistarse)
        self.tiempoEspera(5)

    def validate_error_message(self, expected_message):
        """Valida que aparezca el mensaje de éxito o error esperado."""
        self.tiempoEspera(2)  # Tiempo de espera para garantizar la carga del mensaje
        error_message = self.get_text(MapsObject.validarRegistro)
        assert expected_message in error_message, f"No apareció el mensaje esperado: {expected_message}"

    def login_user(self, email, password):
        """Completa el formulario de login."""
        self.send_keys(MapsObject.txtCorreoLogin, email)
        self.tiempoEspera(2)
        self.send_keys(MapsObject.txtContrasenaLogin, password)
        self.tiempoEspera(2)
        self.click(MapsObject.btnLogin)
        self.tiempoEspera(5)

    def validate_successful_login(self):
        """Valida que el login sea exitoso."""
        user_name = self.get_text(MapsObject.txtNombreMenu)
        assert "prueba aut" in user_name, "El nombre del usuario no coincide."

    def logout_user(self):
        """Cierra sesión."""
        self.click(MapsObject.btnMenu)
        self.tiempoEspera(2)  # Espera después de abrir el menú
        self.click(MapsObject.btnCerrarSesion)
        self.tiempoEspera(5)
