import pytest
from time import sleep
from selenium import webdriver


from pageobjects.contact_page import ContactPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome('resources/chromedriver')
    sleep(5)
    yield driver
    sleep(5)
    driver.quit()

def test_fill_contact_info(browser):
    contact_page = ContactPage(browser)
    contact_page.open()
    contact_page.set_name('Prueba')
    contact_page.set_email('prueba@gmail.com')
    contact_page.set_message('Esta es solo una prueba')


