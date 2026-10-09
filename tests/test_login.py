from selenium.webdriver.common.by import By

from utils.saucedemo_helpers import create_driver, login


def test_login_exitoso():
    driver = create_driver()

    try:
        login(driver)

        assert driver.current_url.endswith("/inventory.html")
        assert driver.title == "Swag Labs"
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    finally:
        driver.quit()
