#  Proyecto de Automatización de Pruebas - SauceDemo

##  Propósito del Proyecto

El objetivo es **automatizar casos funcionales del sitio https://www.saucedemo.com**, verificando el login, la página de productos y el funcionamiento del carrito de compras.

Los casos de prueba fueron desarrollados con **Python**, **Selenium** y **Pytest**.
Las funciones utilizadas para un código más modular están en utils, el chromedriver está en la carpeta drivers.
Los datos usados de usuarios par alogin se acceden leyendo un json en la carpeta datos.
Los archivos principales para las prubeas de automatización están en tests.
Por último los reportes se guardan en carpeta reports.

---

## Tecnologías Utilizadas
- **Python 3.x**
- **Selenium WebDriver**
- **WebDriver Manager**
- **Pytest**
- **Pytest-HTML**

---

## Instalación de Dependencias

1. **Clonar el repositorio**
   git clone https://github.com/Ezequielnbaez/pre-entrega-automation-testing-ezequielbaez
   cd automatizacion-saucedemo

2. **Crear y activar un entorno virtual**
   python -m venv venv
   venv\Scripts\activate

3. **Instalar dependencias**
   pip install -r requirements.txt


## Generar Reporte HTML de Pruebas


**Test de todos los archivos**:
pytest tests/ -v --html=reporte_general.html

**Test automatizaci´pn de login**:
pytest tests/test_automatizacion_login.py -v --html=reporte.html

**Test navegación y verificación**:
pytest tests/test_navegacion_verificacion.py -v --html=reporte.html

**Test interacción de productos(test completo de todos los puntos, login, navegacion y carrito)**:
pytest tests/test_interaccion_productos.py -v --html=reporte.html

**Ezequiel Báez**
Proyecto realizado como parte del curso de Automatización
Año: 2025
