import time

import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from selenium import webdriver

@pytest.mark.usefixtures("browser")
class TestProductBrowsing:
    def setup_method(self):
        """Setup method to initialize the WebDriver instance and pages."""
        self.driver = webdriver.Chrome()
        time.sleep(20)
        self.home_page = HomePage(self.driver)
        time.sleep(20)
        self.product_page = ProductPage(self.driver)

    def test_products_displayed_on_homepage(self):
        """Test to verify if products are displayed on the homepage."""
        products = self.home_page.get_products()
        time.sleep(20)
        assert len(products) > 0, "No products found on the homepage"

    def test_category_navigation(self):
        """Test to navigate through categories and verify product availability."""
        categories = self.home_page.get_categories()
        for category_name in categories:
            self.home_page.navigate_to_category(category_name)
            products = self.home_page.get_products()
            assert len(products) > 0, f"No products found in category: {category_name}"
