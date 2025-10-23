from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.driver_setup import setup_driver
from utils.selenium_func import esperar_visibilidad,escribir_text, click_elemento, obtener_elemento,obtener_texto
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED, TIEMPO_DE_ESPERA

#LOGIN locators
LOC_USER = (By.ID, "user-name")
LOC_PASS = (By.ID, "password")
LOC_BTN_LOGIN = (By.ID, "login-button")
LOC_ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

#PRODUCTOS locators
LOC_PRODUCTOS = (By.CLASS_NAME,"inventory_item")
LOC_ITEM_PRECIO= (By.CLASS_NAME,"inventory_item_price")
LOC_ITEM_NOMBRE= (By.CLASS_NAME,"inventory_item_name")
LOC_TITULO = (By.CLASS_NAME,"title")

#Básicamente se loguea, verifica lista de productos, te muestra el primero con precio y nombre y luego de último el título
def test_nav_ver():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)

        #login con usuario ya verificado
        escribir_text(driver, LOC_USER, USUARIO_PRED)
        escribir_text(driver, LOC_PASS, PASS_PRED)
        click_elemento(driver, LOC_BTN_LOGIN)

        esperar_visibilidad(driver, LOC_PRODUCTOS, TIEMPO_DE_ESPERA)
        print("Login exitoso, cargó catálogo")

        #valida titulo
        titulo=obtener_texto(driver, LOC_TITULO)
        if titulo!="Products":
            print(f"Titulo incorrecto:{titulo}")
        else:
            print(f"Titulo de página validado: {titulo}")
        #verifica lista de products
        productos = obtener_elemento(driver,LOC_PRODUCTOS)

        if not productos:
            print("Productos no encontrados")
        
        else:
            print(f"Se encontraron productos {len(productos)} en el catálogo")
            nombre_elemento=obtener_elemento(driver, LOC_ITEM_NOMBRE)[0]
            precio_elemento=obtener_elemento(driver, LOC_ITEM_PRECIO)[0]
            primer_nombre=nombre_elemento.text
            primer_precio=precio_elemento.text
            print(f"Nombre:{primer_nombre}- Precio:{primer_precio}")

    except TimeoutException as e:
        print(f"Error, algo no cargó a tiempo:{e}")

    except Exception as e:
        print(f"Error general:{e}")
    finally:
        driver.quit()
        print("Fin de prueba Navegación y Verificación del Catálogo")

if __name__ == "__main__":
    test_nav_ver()
