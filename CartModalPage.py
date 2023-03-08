from pages.CartPage import CartPage
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


# Locators and methods for Cart Modal pop-up
class CartModalPage(BasePage):
    MODAL_COMMODITY_VALUE = (By.CSS_SELECTOR, "input[data-testid='modalCountDelivery']")
    BUTTON_DETAILS = (By.XPATH, "//*[text()='Деталі доставки']")
    BUTTON_TO_CART = (By.XPATH, "//*[text()='Оформити замовлення']")

    def go_to_cart_modal(self):
        self.do_click(self.BUTTON_DETAILS)
        return CartModalPage(self.driver)

    def get_cart_value(self):
        if self.is_visible(self.MODAL_COMMODITY_VALUE):
            return self.get_element_attribute(self.MODAL_COMMODITY_VALUE)

    def go_to_cart(self):
        self.do_click(self.BUTTON_TO_CART)
        return CartPage(self.driver)
