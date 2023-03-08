from pages.CommodityPage import CommodityPage
from tests.test_base import BaseTest
from pages.CartModalPage import CartModalPage
import time


# Test to verify if the commodity is in the cart after pressing "Buy" button
class TestCart(BaseTest):

    def test_details_button_visibility(self):
        self.commodityPage = CommodityPage(self.driver)  # Imports commodity page locators and methods
        self.cartModalPage = CartModalPage(self.driver)  # Imports cart modal page locators and methods
        tak_button = self.commodityPage.do_click_tak()   # Clicks on age verification button to proceed
        buy_button = tak_button.do_add_to_cart()  # Clicks on buy button
        cart_modal = buy_button.go_to_cart_modal()  # Checks if details button is displayed and clicks on it
        cart = cart_modal.go_to_cart()  # Clicks on the next button to proceed to the cart
        assert cart.is_commodity_in_cart()  # Check if the added commodity is in the cart
