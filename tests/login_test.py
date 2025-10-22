from utils.selenium_func import escribir_text, click_elemento, obtener_texto, esperar_visibilidad
from utils.config import BASE_URL, TIEMPO_DE_ESPERA
from utils.data_utils import leer_usaurios
from utils.driver_setup import setup_driver
from selenium.common.exceptions import TimeoutException


LOC_USER = ("id", "user-name")
LOC_PASS = ("id", "password")
LOC_BTN_LOGIN = ("id", "login-button")
LOC_ERROR_MSG = ("css selector", "h3[data-test='error']")
LOC_PRODUCTOS = ("class name", "inventory_item")
def test_login():
    usuarios=leer_usaurios()
    driver = setup_driver()

    """Escribe texto y clickea login"""
    try:
        driver.get(BASE_URL)

        for usuario in usuarios:
            #Limpio texto
            escribir_text(driver, LOC_USER, "")
            escribir_text(driver, LOC_PASS, "")
            
            #escribo nuevo
            escribir_text(driver, LOC_USER, usuario["usuario"])
            escribir_text(driver, LOC_PASS, usuario["password"])
            click_elemento(driver, LOC_BTN_LOGIN)

            try: 
                esperar_visibilidad(driver, LOC_PRODUCTOS, TIEMPO_DE_ESPERA)
                print(f"Usuario {usuario['usuario']} logro entrar")
                driver.get(BASE_URL)
                #logra entrar y vuelve al principio
            
            except TimeoutException:
                try:
                    error1 = obtener_texto(driver, LOC_ERROR_MSG)
                    print(f"Usuario {usuario['usuario']} no logro entrar:{error1}")
                except Exception as e:
                    print(f"Usuario {usuario['usuario']} no logro entrar:Error desconocido- {e}")
    except Exception as e:
        print(f"Error general:{e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()