from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Common helpers for all page objects."""

    def __init__(self, driver, wait_seconds: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_seconds)

    def open(self, url: str):
        """Open a URL in the current browser."""
        self.driver.get(url)

    # Accept a locator tuple (By.SOMETHING, value)
    def find_element(self, locator):
        """Find a single element using a locator tuple."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find multiple elements using a locator tuple."""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Click an element referenced by a locator tuple."""
        self.find_element(locator).click()

    def input_text(self, locator, text: str):
        """Clear an input and type text into it."""
        field = self.find_element(locator)
        field.clear()
        field.send_keys(text)

    def wait_for_element(self, locator, timeout=None):
        wait_obj = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait_obj.until(EC.visibility_of_element_located(locator))