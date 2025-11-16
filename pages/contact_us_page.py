
import os
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage(BasePage):
    SOCIAL_MEDIA = (By.CSS_SELECTOR, 'div.text-social')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_contact_us_open(self):
        wait = WebDriverWait(self.driver, timeout=10).until(EC.url_to_be('https://soft.reelly.io/contact-us'))
        assert self.driver.current_url ==  'https://soft.reelly.io/contact-us'

    def verify_social_media(self):
        wait = WebDriverWait(self.driver, timeout=10)
        elements = wait.until(EC.presence_of_all_elements_located(self.SOCIAL_MEDIA))
        assert len(elements) >= 4, f" there are less than 4 social media on the page"




