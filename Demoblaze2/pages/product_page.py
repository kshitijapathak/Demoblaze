from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):

    def add_to_cart(self):
        self.wait_for_clickable(By.CSS_SELECTOR, ".btn-success").click()
        self.wait_for_alert().accept()

    def get_products(self):
        return self.wait_for_elements(By.CLASS_NAME, "card-title")

    def navigate_to_category(self, category_name):
        self.wait_for_clickable(By.XPATH, f"//a[contains(text(), '{category_name}')]").click()
