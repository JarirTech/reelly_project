
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # locators
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
    LOGIN_PAGE_LOCATOR = (By.CSS_SELECTOR, "div.new-market-h1")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, url: str = "https://soft.reelly.io/sign-in"):
        self.open(url)
        self.wait_for_element(self.EMAIL_FIELD)

    def login(self, email: str | None = None, password: str | None = None, timeout: int = 10):
        """
        Perform login.

        - If `email` or `password` are not provided, read from environment variables:
          REELLY_EMAIL and REELLY_PASSWORD.
        - Raises ValueError if credentials are missing.
        """
        email_to_use = email or os.environ.get("REELLY_EMAIL")
        password_to_use = password or os.environ.get("REELLY_PASSWORD")

        if not email_to_use or not password_to_use:
            raise ValueError("Missing credentials: provide email/password or set REELLY_EMAIL and REELLY_PASSWORD environment variables.")

        self.input_text(self.EMAIL_FIELD, email_to_use)
        self.input_text(self.PASSWORD_FIELD, password_to_use)
        self.click(self.LOGIN_BUTTON)

        # Wait until the login page's post-login locator is visible (or timeout)
        self.wait_for_element(self.LOGIN_PAGE_LOCATOR, timeout=timeout)
