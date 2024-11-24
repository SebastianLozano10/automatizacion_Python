# Automatización de Pruebas QA

Este proyecto realiza pruebas automatizadas para la plataforma **Inlaze**, incluyendo los casos de:
- **Registro exitoso**
- **Login exitoso** y cierre de sesión.

---

## **Requisitos**

1. Tener **Python 3.10** o superior instalado en tu máquina.
2. Tener **Google Chrome** instalado.
3. Contar con el **Chromedriver** correspondiente a la versión de Chrome (ya incluido en este proyecto).

---

## **Instalación**

Sigue estos pasos para configurar y ejecutar el proyecto:

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>

2. **Acceder a la carpeta del proyecto**
    cd <NOMBRE_DEL_PROYECTO>

3. **Instalar las dependencias**
    pip install -r requirements.txt

**Ejecución**
1. **Ejecuta el archivo principal del proyecto:**
    python RunPrincipal.py

2. **Selecciona el caso de prueba a ejecutar:**

Ingresa 1 para el caso de Registro Exitoso.
Ingresa 2 para el caso de Login Exitoso y Cerrar Sesión.
Ingresa 3 para ejecutar ambos casos de prueba.

**Resultados**

1. Durante la ejecución, el programa generará capturas de pantalla que se guardarán en la carpeta screenshots/.
2. Al finalizar, se generará un archivo PDF (Automatizacion_Resultados.pdf) en la carpeta screenshots/ que incluirá todas las capturas.

**Estructura del Proyecto**

Prueba Tecnica Python/
│
├── base/                     # Clases base para la automatización.
├── maps/                     # Mapas de objetos utilizados en las pruebas.
├── pag/                      # Métodos asociados a las páginas.
├── pom.json                  # Archivo de configuración.
├── requirements.txt          # Dependencias necesarias.
├── screenshots/              # Carpeta donde se guardan las capturas y el PDF.
├── utils/                    # Funciones utilitarias (limpiar capturas, etc.).
├── RunPrincipal.py           # Script principal de ejecución.
├── README.md                 # Documentación del proyecto.


**Consideraciones**

1. Limpieza automática: Antes de ejecutar las pruebas, el proyecto elimina todas las capturas y el PDF anteriores de la carpeta screenshots/.
2. Internet y enlaces activos: Asegúrate de tener acceso a internet y de que los enlaces de prueba estén activos.

**Bug o posibles mejoras**

- pude visualizar que permite realizar el registro con datos ya existentes deberia arrojar un error
- en el desarrollo habian alguno elementos que no conteian un ID o un name