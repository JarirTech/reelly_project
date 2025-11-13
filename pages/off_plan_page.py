from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep


class OffPlanPage(BasePage):
    def __init__(self, driver):       # constructor inherited from BasePage
        super().__init__(driver)

    OFF_PLAN_BUTTON = (By.CSS_SELECTOR,
                       '#w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b > div.menu-block > a:nth-child(2) > div.div-block-121 > div.g-menu-text')

    def click_on_off_plan(self):
        wait = WebDriverWait(self.driver, 10)  # wait up to 10 seconds
        element = wait.until(EC.element_to_be_clickable(self.OFF_PLAN_BUTTON))

        element.click()

    def verify_page_open(self):
        #old_url = self.driver.current_url
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://find.reelly.io/?pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1"))

        assert self.driver.current_url == "https://find.reelly.io/?pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1"


    def verify_product_title_img(self):

        try:
            product_cards = self.driver.find_elements(By.CSS_SELECTOR, 'a[class="outline-none w-full"]')
            assert product_cards, " No product items were found on the page."

            for index, item in enumerate(product_cards, start=1):
                try:
                    title = item.find_element(By.CSS_SELECTOR, 'h4[title]')
                    image = item.find_element(By.TAG_NAME, "img")

                    assert title.text.strip() != "", f" Product {index} is missing a title."
                    assert image.get_attribute("src"), f" Product {index} is missing an image src."
                except Exception as e:
                    raise AssertionError(f" Error in product {index}: {str(e)}")
            return True
        except Exception as e:
            raise AssertionError(f" Failed while verifying all products: {str(e)}")



