from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.saucedemo_helpers import create_driver, get_inventory_products, login


def test_agregar_producto_al_carrito():
    driver = create_driver()

    try:
        login(driver)

        products = get_inventory_products(driver)
        assert len(products) > 0

        first_product = products[0]
        product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
        first_product.find_element(By.CSS_SELECTOR, "button").click()

        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1"

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) > 0
        assert product_name in driver.page_source

    finally:
        driver.quit()
