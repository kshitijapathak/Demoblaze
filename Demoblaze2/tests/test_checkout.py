import time
import pytest
from pages.home_page import HomePage
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    """
    Fixture to initialize the WebDriver instance before the test module and quit it after the tests.

    Returns:
        WebDriver: An instance of the Chrome WebDriver.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_checkout(driver):
    """
    Test case to verify the successful checkout process.

    Steps:
        1. Navigate to the last product on the home page.
        2. Add the product to the cart.
        3. Proceed to the checkout page.
        4. Fill in the order details.
        5. Place the order.
        6. Verify if the order confirmation message is displayed.

    Args:
        driver (WebDriver): The WebDriver instance.

    """
    home_page = HomePage(driver)

    home_page.navigate_to_last_product()
    time.sleep(20)
    home_page.add_to_cart()
    time.sleep(20)
    cart_page = home_page.go_to_cart()

    items_in_cart = cart_page.get_cart_items()
    assert len(items_in_cart) > 0, "Items are not added to the cart"

    checkout_page = cart_page.proceed_to_checkout()

    checkout_page.fill_order_details("kshitija", "India", "Pune", "1234567890", "01", "2025")
    checkout_page.place_order()
    time.sleep(20)

    assert checkout_page.is_order_confirmation_displayed(), "Order confirmation message is not displayed"
