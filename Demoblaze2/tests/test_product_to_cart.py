import time
import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("browser")
class TestAddProductToCart:
    """Test case for adding a product to the cart."""

    def test_add_to_cart(self, browser):
        """Test to verify that a product can be added to the cart."""
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        time.sleep(20)

        # Navigate to the last product on the homepage
        home_page.navigate_to_last_product()
        time.sleep(20)

        # Add the product to the cart
        cart_page.add_to_cart()
        time.sleep(20)

        # Go to the cart page
        cart_page.go_to_cart()
        time.sleep(20)

        # Get the items in the cart
        cart_items = cart_page.get_cart_items()

        # Assert that the cart has items
        assert len(cart_items) > 0, "No items found in the cart"
