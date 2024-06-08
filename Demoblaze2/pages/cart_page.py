from selenium.webdriver.common.by import By
from .base_page import BasePage
from pages.checkoutpage import CheckoutPage



class CartPage(BasePage):
    def add_to_cart(self):
        self.wait_for_clickable(By.CSS_SELECTOR, ".btn-success").click()
        self.wait_for_alert().accept()

    def go_to_cart(self):
        self.wait_for_clickable(By.ID, "cartur").click()

    def get_cart_items(self):
        return self.wait_for_elements(By.CSS_SELECTOR, ".success")

    def proceed_to_checkout(self):
        checkout_button = self.wait_for_clickable(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        checkout_button.click()
        return CheckoutPage(self.driver)
