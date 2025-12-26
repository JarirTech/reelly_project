from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#PASSWORD_URL = "https://soft.reelly.io/set-new-password"
class ChangePasswordPage(BasePage):
    PASSWORD_URL = "https://soft.reelly.io/set-new-password"
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Enter new password"]')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Repeat password"]')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[wized="changePasswordButton"]')

    def __init__(self, driver):
        super().__init__(driver)


    def verify_password_page_opens(self):
        assert self.wait.until(EC.url_to_be(self.PASSWORD_URL)), \
            f"Expected URL to be {self.PASSWORD_URL}, but got {self.driver.current_url}"


    def test_password_field(self):
        self.input_text(self.PASSWORD_FIELD, "test")
        self.input_text(self.REPEAT_PASSWORD, "test")

    def verify_change_password_button(self):
        assert self.wait.until(EC.element_to_be_clickable(self.CHANGE_PASSWORD_BUTTON)), f" the Button is not there"