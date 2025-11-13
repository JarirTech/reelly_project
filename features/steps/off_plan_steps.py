import os
from behave import given, when, then
from app.application import Application


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
