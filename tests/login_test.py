from utils.selenium_func import escribir_text, click_elemento, obtener_texto
from utils.config import BASE_URL
from utils.data_utils import leer_usaurios
from utils.driver_setup import setup_driver

LOC_USER = ("id", "user-name")
LOC_PASS = ("id", "password")
LOC_BTN_LOGIN = ("id", "login-button")
LOC_ERROR_MSG = ("css selector", "h3[data-test='error']")
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
            escribir_text(driver, LOC_USER, usuario["password"])
            click_elemento(driver, LOC_BTN_LOGIN)

            try: 
                print("Usuario '{usuario['usuario']}' logro entrar")
                driver.get(BASE_URL)
                #logra entrar y vuelve al principio
            
            except TimeoutError:
                try:
                    error = obtener_texto(driver, LOC_ERROR_MSG)
                    print("Usuario '{usuario['usuario']}' no logro entrar:{error}")
                except:
                    print("Usuario '{usuario['usuario']}' no logro entrar:Error desconocido")

    finally:
        driver.quit()