from fpdf import FPDF
import os

class PDFUtils:
    def __init__(self, output_path="screenshots/Automatizacion_Resultados.pdf"):
        self.pdf = FPDF()
        self.output_path = output_path

    def limpiar_pdf(self):
        """Elimina el PDF anterior si existe."""
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
            print(f"Se eliminó el PDF previo: {self.output_path}")

    def agregar_encabezado(self, automator_name, base_url):
        """Agrega un encabezado al PDF."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", style="B", size=14)
        self.pdf.cell(0, 10, "Reporte de Automatización", ln=True, align="C")
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(0, 10, f"Automatizador: {automator_name}", ln=True, align="C")
        self.pdf.cell(0, 10, f"URL Base: {base_url}", ln=True, align="C")
        self.pdf.ln(10)  # Espacio después del encabezado

    def agregar_imagen(self, image_path, title):
        """Agrega una imagen con un marco y título."""
        if os.path.exists(image_path):
            self.pdf.set_font("Arial", size=10)
            self.pdf.cell(0, 10, title, ln=True, align="C")
            self.pdf.set_draw_color(0, 0, 0)  # Color del marco
            self.pdf.rect(10, self.pdf.get_y() + 5, 190, 110)  # Marco alrededor de la imagen
            self.pdf.image(image_path, x=15, y=self.pdf.get_y() + 10, w=180)  # Agregar la imagen dentro del marco
            self.pdf.ln(120)  # Espacio después de la imagen
        else:
            print(f"Imagen no encontrada: {image_path}")

    def generar_pdf(self):
        """Genera y guarda el PDF."""
        self.pdf.output(self.output_path)
        print(f"PDF generado: {self.output_path}")
