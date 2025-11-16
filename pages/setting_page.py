
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class SettingPage(BasePage):


    CONTACT_US_BUTTON=(By.XPATH, '//div[@class="setting-text" and text()="Contact us"]')
    CONNECT_BUTTON = (By.XPATH, '//div[@class="get-free-period menu" and text()="Connect the company"]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_on_contact_us(self):
        self.click(self.CONTACT_US_BUTTON)

    def connect_button(self):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.element_to_be_clickable(self.CONNECT_BUTTON))
        assert element, f' the connect button not clickable'

