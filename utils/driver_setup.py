from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver(headless=False):
    """Configuración de una instancia de chrome Webdrive"""

    chrome_options=Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-dev-shm-usage")

    service = Service()

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver