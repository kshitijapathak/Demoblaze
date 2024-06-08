import unittest
import time
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import read_login_data
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    """
    Test the login functionality.

    Steps:
    1. Navigate to the login page.
    2. Enter the username and password.
    3. Submit the login form.
    4. Verify the welcome message or alert message.
    """

    def setUp(self):
        """Setup the test environment."""
        self.driver = webdriver.Chrome()
        time.sleep(20)
        self.home_page = HomePage(self.driver)
        time.sleep(20)
        self.login_page = LoginPage(self.driver)

    def test_login_functionality(self):
        """Test the login functionality with different login data."""
        for username, password, success in read_login_data("data/test_data_login.json"):
            time.sleep(10)
            self.home_page.go_to_login()
            time.sleep(10)
            self.login_page.enter_username(username)
            self.login_page.enter_password(password)
            time.sleep(10)
            self.login_page.submit_login()

            if success:
                time.sleep(20)
                welcome_message = self.login_page.get_welcome_message()
                self.assertEqual(welcome_message, f"Welcome {username}")
                self.login_page.logout()
                response_logout = self.login_page.wait_for_element(By.ID, "nava")
                self.assertEqual(response_logout.text, "PRODUCT STORE")
            else:
                try:
                    time.sleep(20)
                    response_data = self.login_page.wait_for_alert()
                    response_text = response_data.text
                    self.driver.switch_to.alert.accept()
                    self.assertIn(response_text, ["Wrong password.", "User does not exist."])
                except:
                    self.fail("Alert not found or wrong message")

    def test_blank_username_and_password(self):
        """Test login with blank username and password."""
        self.home_page.go_to_login()
        time.sleep(20)
        self.login_page.enter_username("")
        self.login_page.enter_password("")
        time.sleep(20)
        self.login_page.submit_login()
        time.sleep(20)
        alert = self.login_page.wait_for_alert()
        self.assertIn("Please fill out Username and Password.", alert.text)

    def tearDown(self):
        """Clean up after the test."""
        self.driver.quit()
