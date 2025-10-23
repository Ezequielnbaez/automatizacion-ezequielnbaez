from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.driver_setup import setup_driver
from utils.selenium_func import esperar_visibilidad,escribir_text, click_elemento, obtener_elemento,obtener_texto
from utils.config import BASE_URL, USUARIO_PRED, PASS_PRED, TIEMPO_DE_ESPERA

#LOGIN locators
LOC_USER = (By.ID, "user-name")
LOC_PASS = (By.ID, "password")
LOC_BTN_LOGIN = (By.ID, "login-button")

#PRODUCTOS locators
LOC_PRODUCTOS = (By.CLASS_NAME,"inventory_item")
LOC_ITEM_PRECIO= (By.CLASS_NAME,"inventory_item_price")
LOC_ITEM_NOMBRE= (By.CLASS_NAME,"inventory_item_name")
LOC_BTN_ADD_CART = (By.CLASS_NAME,"btn_inventory")
LOC_CART_BADGE = (By.CLASS_NAME,"shopping_cart_badge")
LOC_CART_LINK = (By.CLASS_NAME,"shopping_cart_link")
LOC_CART_ITEMS = (By.CLASS_NAME,"cart_item")

#Básicamente se loguea, verifica lista de productos, te muestra el primero con precio y nombre y luego de último el título
def test_carrito():
    driver = setup_driver()
    try:
        driver.get(BASE_URL)

        #login con usuario ya verificado
        escribir_text(driver, LOC_USER, USUARIO_PRED)
        escribir_text(driver, LOC_PASS, PASS_PRED)
        click_elemento(driver, LOC_BTN_LOGIN)

        esperar_visibilidad(driver, LOC_PRODUCTOS, TIEMPO_DE_ESPERA)
        print("Login exitoso, cargó catálogo")

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

            #Agrego al carrito
            click_elemento(driver, LOC_BTN_ADD_CART)
            print(f"Producto '{primer_nombre}' agregado al carrito")

            #contador del carrito
            contador = obtener_texto(driver, LOC_CART_BADGE)
            if contador != "1":
                print(f"Error: contador incorrecto {contador}")
            
            else:
                #Navega al carrito
                click_elemento(driver, LOC_CART_LINK)
                esperar_visibilidad(driver, LOC_CART_ITEMS, TIEMPO_DE_ESPERA)

                #Verifica producto en carrito
                item_carrito = obtener_elemento(driver,LOC_CART_ITEMS)[0]
                nombre_en_carrito = item_carrito.find_element(By.CLASS_NAME,"inventory_item_name").text
                if nombre_en_carrito == primer_nombre:
                    print("Producto correctamente agregado al carrito")
                else:
                    print(f"Error: producto incorrecto:{nombre_en_carrito}")


    except TimeoutException as e:
        print(f"Error, algo no cargó a tiempo:{e}")

    except Exception as e:
        print(f"Error general:{e}")
    finally:
        driver.quit()
        print("Fin de prueba Navegación y Verificación del Catálogo")

if __name__ == "__main__":
    test_carrito()
