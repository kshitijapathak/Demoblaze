import pytest
import time
from selenium import webdriver
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.helpers import read_signup_data

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.signup_page = SignupPage(driver)
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestSignup:
    def test_signup_functionality(self):
        """
                Test signup functionality.

                Steps:
                1. Navigate to the signup page.
                2. Enter the username and password.
                3. Submit the signup form.
                4. Verify the alert message.

                Parameters:
                username (str): The username to use for signup.
                password (str): The password to use for signup.
                success (bool): Expected success status of signup.
                """
        for username, password, success in read_signup_data("data/test_data_signup.json"):
            time.sleep(20)
            self.home_page.go_to_signup()
            self.signup_page.enter_username(username)
            self.signup_page.enter_password(password)
            time.sleep(20)
            self.signup_page.submit_signup()

            try:
                time.sleep(20)
                alert = self.signup_page.wait_for_alert()
                alert_text = alert.text
                alert.accept()

                if success:
                    time.sleep(20)
                    assert alert_text == "Sign up successful."
                else:
                    time.sleep(20)
                    assert alert_text == "This user already exists."
            except Exception as e:
                time.sleep(20)
                pytest.fail(f"Alert not found or wrong message: {e}")

    def test_signup_blank_username_password(self):
        """
        Test signup with blank username and password.

        Steps:
        1. Navigate to the signup page.
        2. Leave the username and password fields blank.
        3. Submit the signup form.
        4. Verify the alert message.

        Expected Result:
        The alert message should indicate that the username and password cannot be blank.
        """
        time.sleep(20)
        self.home_page.go_to_signup()
        self.signup_page.enter_username("")
        self.signup_page.enter_password("")
        time.sleep(20)
        self.signup_page.submit_signup()

        try:
            time.sleep(20)
            alert = self.signup_page.wait_for_alert()
            alert_text = alert.text
            alert.accept()

            # Adjust this assertion based on the actual alert message your application shows for blank inputs
            assert alert_text == "Please fill out Username and Password."
        except Exception as e:
            time.sleep(20)
            pytest.fail(f"Alert not found or wrong message: {e}")
