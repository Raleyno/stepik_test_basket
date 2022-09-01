from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

#def go_to_login_page(browser):
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

def test_guest_can_add_product_to_basket(browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        
	# pytest -s -v --tb=line --language=en test_product_page.py 	- запуск этого теста