# checkout_page.py
import time

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_order_details(self, name, country, city, card_number, month, year):
        time.sleep(20)
        name_field = self.wait_for_element(By.ID, "name")
        time.sleep(10)
        name_field.send_keys(name)
        time.sleep(10)
        country_field = self.wait_for_element(By.ID, "country")
        time.sleep(10)
        country_field.send_keys(country)
        time.sleep(10)
        city_field = self.wait_for_element(By.ID, "city")
        time.sleep(10)
        city_field.send_keys(city)
        time.sleep(10)
        card_field = self.wait_for_element(By.ID, "card")
        time.sleep(10)
        card_field.send_keys(card_number)
        time.sleep(10)
        month_field = self.wait_for_element(By.ID, "month")
        time.sleep(10)
        month_field.send_keys(month)
        time.sleep(10)
        year_field = self.wait_for_element(By.ID, "year")
        time.sleep(10)
        year_field.send_keys(year)

    def place_order(self):
        # Locate the place order button and click it
        time.sleep(20)
        place_order_button = self.wait_for_clickable(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
        time.sleep(10)
        place_order_button.click()

    def is_order_confirmation_displayed(self):
        time.sleep(20)
        confirmation_message_locator = (By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]")
        time.sleep(20)
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(confirmation_message_locator)
        )
        return confirmation_message.is_displayed()