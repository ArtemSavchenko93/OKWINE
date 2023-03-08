from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData
from pages.CartModalPage import CartModalPage


# Locators and methods for a Commodity page (Сторінка товару)
class CommodityPage(BasePage):
    BUTTON_BUY = (By.XPATH, "//*[text()='Додати до кошика']")
    BUTTON_DETAILS = (By.XPATH, "//*[text()='Деталі доставки']")
    MODAL_BUTTON_TAK = (By.XPATH, "//*/a/button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_add_to_cart(self):
        self.do_click(self.BUTTON_BUY)
        return CommodityPage(self.driver)

    def go_to_cart_modal(self):
        self.do_click(self.BUTTON_DETAILS)
        return CartModalPage(self.driver)

    def is_button_details_visible(self):
        return self.is_visible(self.BUTTON_DETAILS)

    def is_button_buy_visible(self):
        return self.is_visible(self.BUTTON_BUY)

    def do_click_tak(self):
        self.do_click(self.MODAL_BUTTON_TAK)
        return CommodityPage(self.driver)
