from selenium.webdriver.common.by import By

from utils.saucedemo_helpers import create_driver, get_first_product_data, get_inventory_products, login


def test_catalogo_inventario():
    driver = create_driver()

    try:
        login(driver)

        assert driver.title == "Swag Labs"

        products = get_inventory_products(driver)
        assert len(products) > 0

        first_name, first_price = get_first_product_data(driver)
        assert first_name == "Sauce Labs Backpack"
        assert first_price == "$29.99"

        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

    finally:
        driver.quit()
