from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_visibilidad(driver, locator, tiempo=10):
    """Para comprobar que existan elementos visibles en la página dentro de 10s"""
    return WebDriverWait(driver, tiempo).until(EC.visibility_of_element_located(locator))


def escribir_text(driver, locator, texto):
    """Escribe texto, por ejemplo, para el login"""
    elemento = esperar_visibilidad(driver,locator)
    elemento.clear()
    elemento.send_keys(texto)

def esperar_clickeable(driver, locator, tiempo=10):
    """Espera a que un elemento se pueda dar click dentro de los 10s"""
    return WebDriverWait(driver, tiempo).until(EC.element_to_be_clickable(locator))

def click_elemento(driver,locator):
    """Clickea el elemento una vez que se verifica que es clickeable"""
    elemento = esperar_clickeable(driver,locator)
    elemento.click()
    

def obtener_texto(driver, locator):
    elemento = esperar_visibilidad(driver, locator)
    return elemento.tex