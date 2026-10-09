from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://www.saucedemo.com"


def create_driver():
    """Crea un navegador Chrome y configura una ejecución headless."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1200")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)


def login(driver, username="standard_user", password="secret_sauce"):
    """Inicia sesión en SauceDemo con credenciales válidas."""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("/inventory.html"))
    return driver


def get_inventory_products(driver):
    """Devuelve todos los productos visibles en el catálogo."""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "inventory_item")))
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def get_first_product_data(driver):
    """Obtiene el nombre y el precio del primer producto visible."""
    products = get_inventory_products(driver)
    assert products, "No se encontraron productos en el catálogo."

    first_product = products[0]
    name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
    return name, price
