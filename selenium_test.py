from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized") 

service = Service("drivers/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")

print("Título de la página:", driver.title)

driver.quit()