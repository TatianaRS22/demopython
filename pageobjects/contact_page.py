from selenium.webdriver.common.by import By
import time
from pageobjects.base_page import BasePage
import allure
import pyautogui

class ContactPage(BasePage):
    URL = 'http://softesting.com/Test/'
    CONTACTO = (By.XPATH, '//*[@id="menu-item-1031"]/a')
    TRABAJA = (By.XPATH, '//*[@id="menu-item-1039"]/a')
    NAME_ID = (By.ID, 'nf-field-12')
    EMAIL_ID = (By.ID, 'nf-field-13')
    MSG_ID = (By.ID, 'nf-field-14')
    NAME= (By.ID, 'nf-field-18')
    MODALIDAD = (By.XPATH, '//*[@id="menu-item-1083"]/a')
    COMPONENTES = (By.XPATH, '//*[@id="menu-item-1022"]/a')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(5)

    def contact(self):
        self.driver.find_element(*self.CONTACTO).click()
        pyautogui.press('space')
        allure.attach(self.driver.get_screenshot_as_png(), name='CONTACTO', attachment_type=allure.attachment_type.PNG)
        allure.attach('Pagina de contacto', name='attachment contacto', attachment_type=allure.attachment_type.TEXT)
        time.sleep(5)

    def trabaja(self):
        self.driver.find_element(*self.TRABAJA).click()
        pyautogui.press('space')
        allure.attach(self.driver.get_screenshot_as_png(), name='TRABAJA CON NOSOTROS', attachment_type=allure.attachment_type.PNG)
        allure.attach("Texto informativo")
        time.sleep(5)

    def set_name(self, name):
        self.driver.find_element(*self.NAME_ID).send_keys(name)
        allure.attach(self.driver.get_screenshot_as_png(), name='NOMBRE', attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_ID).send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(), name='EMAIL', attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def set_message(self, message):
        self.driver.find_element(*self.MSG_ID).send_keys(message)
        time.sleep(5)

    def set_namet(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)
        pyautogui.write('hello')
        time.sleep(5)

    def servicio(self):
        pyautogui.click('Ima/serviciossof.png')
        time.sleep(5)
        #time.sleep(5)
        self.driver.find_element(*self.MODALIDAD).click()
        #pyautogui.click('Ima/modalidad.png')
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name='MODALIDAD', attachment_type=allure.attachment_type.PNG)

    def recorrido(self):
        pyautogui.press('space')
        pyautogui.press('space')
        time.sleep(3)
        pyautogui.click('Ima/subir.png')
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name='RECORRIDO', attachment_type=allure.attachment_type.PNG)

    def iniciosof(self):
        pyautogui.click('Ima/logosof.png')
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name='INICIO', attachment_type=allure.attachment_type.PNG)

    def chat(self):
        time.sleep(5)
        #button7point = pyautogui.center('Ima/chatsof.png')
        #button7x, button7y = button7point
        #pyautogui.click(button7x, button7y)
        #pyautogui.click('Ima/chatsof.png')
        button7location = pyautogui.locateOnScreen('Ima/chatsof.png', confidence=0.9)
        #print(button7location)
        button7point = pyautogui.center(button7location)
        button7x, button7y = button7point
        pyautogui.click(button7x, button7y)
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name='CHAT', attachment_type=allure.attachment_type.PNG)

    def mensajechat(self):
        pyautogui.write('Prueba mensaje chat')
        allure.attach(self.driver.get_screenshot_as_png(), name='MENSAJE CHAT', attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        #pyautogui.click('Ima/cerrarchatsof.png')
        button6location = pyautogui.locateOnScreen('Ima/cerrarchatsof.png', confidence=0.9)
       # print(button6location)
        allure.attach('button6location', name='attachment contacto', attachment_type=allure.attachment_type.TEXT)
        button6point = pyautogui.center(button6location)
        button6x, button6y = button6point
        pyautogui.click(button6x, button6y)
        time.sleep(5)

    def componentesservicio(self):
        pyautogui.click('Ima/serviciossof.png')
        time.sleep(5)
        self.driver.find_element(*self.COMPONENTES).click()
        time.sleep(5)

    def componentes(self):
        pyautogui.click('Ima/personal.png')
        pyautogui.click('Ima/metodologia.png')
        pyautogui.click('Ima/herramientas.png')
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name='COMPONENTES', attachment_type=allure.attachment_type.PNG)
