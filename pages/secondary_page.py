import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class SecondaryPage(BasePage):
    SECONDARY_URL= "https://soft.reelly.io/secondary-listings"

    FILTER_BUTTON = (By.CSS_SELECTOR, 'div.filter-button')
    WANT_TO_SELL_BUTTON = (By.XPATH, '//div[@class="tag-text-filters" and text()="Want to sell"]')
    APPLY_FILTER = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')
    LISTING_BUTTON = (By.XPATH, '//div[@class="page-title listing" and text()= "Listings"]')
    AGENTS_BUTTON = (By.XPATH, '//div[@class="page-title listing" and text()= "Agents"]')

    def __init__(self,driver):
        super().__init__(driver)

    def verify_secondary_page_opens(self):
        wait = WebDriverWait(self.driver, timeout=10).until(EC.url_to_be("https://soft.reelly.io/secondary-listings"))
        assert self.driver.current_url == "https://soft.reelly.io/secondary-listings", f'page not found'

    def click_filter_button(self):
        self.click(self.FILTER_BUTTON)

    def clicking_want_to_sell_button(self):
        self.click(self.WANT_TO_SELL_BUTTON)

    def clicking_apply_filter(self):
        self.click(self.APPLY_FILTER)

    def verify_want_to_sell_filter(self):


        listing_el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LISTING_BUTTON)
        )
        agents_el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.AGENTS_BUTTON)
        )

        assert listing_el.text.strip() == "Listings", "Listings button text is incorrect"
        assert agents_el.text.strip() == "Agents", "Agents button text is incorrect"

    def scroll_down(self):
        actions = ActionChains(self.driver)

        # Scroll down (large amount)
        actions.scroll_by_amount(0, 20000).perform()

    def scroll_up(self):
        # Scroll back up
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, -20000).perform()