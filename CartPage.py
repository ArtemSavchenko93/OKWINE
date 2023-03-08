from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


# Locators and methods for operation with a Cart Page
class CartPage(BasePage):
    COMMODITY = (By.XPATH, "//*[text()='Ром Дед Менс Фінгерс (ДМФ), Малина / Dead Man’s Fingers (DMF), Raspberry, "
                           "37.5%, 0.7л']")

    def is_commodity_in_cart(self):
        return self.is_visible(self.COMMODITY)
