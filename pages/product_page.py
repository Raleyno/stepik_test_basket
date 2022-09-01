from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
    # название книги и ее цена:
        self.book = (self.browser.find_element(*ProductPageLocators.BOOK)).text
        self.price = (self.browser.find_element(*ProductPageLocators.PRICE)).text
        add_btn.click()
        self.solve_quiz_and_get_code()
    # название книги и ее цена в корзине:
        self.book_in_basket = (self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET)).text
        self.price_in_basket = (self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)).text
    # сравнить заказ и корзину:
        self.should_be_same_book()

    def should_be_same_book(self):
        time.sleep(3)
        assert self.book == self.book_in_basket, "В корзине нет добавленного товара"
        assert self.price == self.price_in_basket, "Цена товара не совпадает с ценой добавленного товара"
        