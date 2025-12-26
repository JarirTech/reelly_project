from pages.base_page import BasePage
from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage
from pages.setting_page import  SettingPage
from pages.contact_us_page import ContactUsPage
from pages.secondary_page import SecondaryPage
from pages import change_password_page


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.setting_page =  SettingPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.change_password_page = ChangePasswordPage(driver)



