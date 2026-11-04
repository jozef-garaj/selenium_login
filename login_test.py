from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def main():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        driver.get(LOGIN_URL)

        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)

        login_button = driver.find_element(By.ID, "login-button")
        assert login_button.is_enabled(), "Login button is disabled"
        login_button.click()

        title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".title"))
        )
        assert title.text == "Products", f"Unexpected page title: {title.text!r}"
        print("Login successful")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
