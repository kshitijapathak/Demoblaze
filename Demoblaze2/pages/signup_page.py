from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )

    def enter_username(self, username):
        username_field = self.wait_for_element(By.ID, "sign-username")
        username_field.clear()  # Clear any existing text
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait_for_element(By.ID, "sign-password")
        password_field.clear()  # Clear any existing text
        password_field.send_keys(password)

    def submit_signup(self):
        signup_button = self.wait_for_element(By.XPATH, "//button[contains(text(),'Sign up')]")
        signup_button.click()

    def wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return self.driver.switch_to.alert
