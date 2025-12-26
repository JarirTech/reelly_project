import os
from unittest.util import three_way_cmp

from behave import given, when, then
from app.application import Application

#  Scenario: User can see titles and pictures on each product inside the off plan page
@given('Open the main page')
def open_main_page_step(context):
    context.app = Application(context.driver)
    context.app.base_page.open('https://soft.reelly.io/sign-in')


@when('Log in to the login page')
def login_steps(context):
    # Read credentials from environment variables
    email = os.environ.get("REELLY_EMAIL")
    password = os.environ.get("REELLY_PASSWORD")

    if not email or not password:
        raise ValueError(
            "Missing credentials: please set REELLY_EMAIL and REELLY_PASSWORD environment variables."
        )

    context.app.login_page.login(email, password)


@when('Click on “off plan” at the left side menu.')
def click_on_steps(context):
    context.app.off_plan_page.click_on_off_plan()


@then('Verify the right page opens.')
def verify_page_steps(context):
    context.app.off_plan_page.verify_page_open()


@then('Verify each product on this page contains a title and picture visible.')
def verify_product_title_img_steps(context):
    context.app.off_plan_page.verify_product_title_img()
#Scenario: User can open the Contact us page
@when ('Clicking on the Setting icon on the left of the page.')
def clicking_settings_steps(context):
    context.app.login_page.clicking_settings_icon()
@when ('Click on Contact us tab.')
def clicking_on_contact_us_steps(context):
    context.app.setting_page.click_on_contact_us()

@then ('Verify Contact us page opens.')
def verify_contact_us_open_steps(context):
    context.app.contact_us_page.verify_contact_us_open()

@then('Verify that there are at least 4 social media icons.')
def verify_social_media_steps(context):
    context.app.contact_us_page.verify_social_media()
@then ('Verify that "connect the company" button is available and clickable.')
def connect_button_steps(context):
    context.app.setting_page.connect_button()

#Scenario 3:
@when ('Click on "Secondary" option at the left side menu')
def clicking_on_secondary_button(context):
    context.app.login_page.clicking_on_secondary_button()
@then('Verify the secondary page opens.')
def verify_secondary_page_opens_steps(context):
    context.app.secondary_page.verify_secondary_page_opens()

@then('Click on filter icon.')
def click_filter_button_steps(context):
    context.app.secondary_page.click_filter_button()


@then ('Click on "want to sell" button.')
def clicking_want_to_sell_steps(context):
    context.app.secondary_page.clicking_want_to_sell_button()

@then ('Click on "Apply filter" button.')
def apply_filter_steps(context):
    context.app.secondary_page.clicking_apply_filter()

@then('Verify "Listings" and "Agents" exist.')
def verify_want_to_sell_filter_steps(context):
    context.app.secondary_page.verify_want_to_sell_filter()
#------------------------------------------------------------------------------------------------

#scenario 4:
@when('Go to the bottom of the page.')
def scroll_down_steps(context):
    context.app.secondary_page.scroll_down()
@then ('Verify the pagination section at the bottom of the page is visible.')
def verify_pagination_steps(context):
    context.app.secondary_page.verify_pagination()

@then('Go back to the top of the page.')
def scroll_up_steps(context):
    context.app.secondary_page.scroll_up()
@then ('Verify the grid_menu is visible.')
def grid_menu_steps(context):
    context.app.secondary_page.verify_top_page()


#-------------------------------------------------------------------------------------------------------------
#scenario 5:
@when ('Click on change password button.')
def clicking_change_password_steps(context):
    context.app.setting_page.clicking_change_password()

@then('Verify the password page opens.')
def verify_password_page(context):
    context.app.change_password_page.verify_password_page_opens()

@then('Add some test password into the input fields.')

def changing_password_steps(context):
    context.app.change_password_page.test_password_field()
@then('Verify the "change password" button is available.')
def verify_change_password_button_steps(context):
    context.app.change_password_page.verify_change_password_button()

