from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def enter_username(self, username):
        self.wait_for_element(By.ID, "loginusername").send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(By.ID, "loginpassword").send_keys(password)

    def submit_login(self):
        self.wait_for_clickable(By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[2]").click()

    def get_welcome_message(self):
        return self.wait_for_element(By.ID, "nameofuser").text

    def logout(self):
        self.wait_for_clickable(By.ID, "logout2").click()
