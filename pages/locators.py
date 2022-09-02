from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")       # кнопка добавить в корзину
    BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")            # название книги
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")         # заказанная книга в корзине
    PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")         # цена книги       
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")      # цена заказанной книги в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")               # успешно добавлено в корзину 