import time
from .cart_page import CartPage
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()

    def go_to_signup(self):
        self.wait_for_clickable(By.ID, "signin2").click()

    def go_to_login(self):
        self.wait_for_clickable(By.ID, "login2").click()

    def get_products(self):
        time.sleep(20)
        return self.wait_for_elements(By.CLASS_NAME, "card-title")

    def get_categories(self):
        time.sleep(20)
        return [category.text for category in self.wait_for_elements(By.CLASS_NAME, "list-group-item")]

    def navigate_to_category(self, category_name):
        time.sleep(20)
        self.wait_for_clickable(By.XPATH, f"//a[contains(text(), '{category_name}')]").click()

    def navigate_to_last_product(self):
        while True:
            try:
                next_button = self.wait_for_clickable(By.ID, "next2", timeout=20)
                next_button.click()
                self.wait_for_element_staleness(next_button)
            except:
                break
        products = self.wait_for_elements(By.CSS_SELECTOR, ".hrefch", timeout=20)
        last_product = products[-1]
        last_product.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait_for_clickable(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        add_to_cart_button.click()
        self.wait_for_alert().accept()

    def go_to_cart(self):
        cart_button = self.wait_for_clickable(By.ID, "cartur")
        cart_button.click()
        return CartPage(self.driver)