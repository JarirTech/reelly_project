

# features/environment.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
load_dotenv()

from app.application import Application

def browser_init(context):
    """Create a new ChromeDriver for a scenario and attach helper objects to context."""
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Toggle headless via environment variable if needed (useful for CI)
    if os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument("--headless=new")

    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(4)

    # create application wrapper AFTER driver exists
    context.app = Application(context.driver)
    print("Browser started for scenario")

def before_all(context):
    """Global setup for the test run. Do NOT create a browser here."""
    print("before_all: global setup (no browser started)")

def before_scenario(context, scenario):
    print(f"\nStarted scenario: {scenario.name}")
    browser_init(context)

def before_step(context, step):
    print(f"\nStarted step: {step.name}")

def after_step(context, step):
    if step.status == 'failed':
        print(f"\nStep failed: {step.name}")

def after_scenario(context, scenario):
    print(f"Ending scenario: {scenario.name}")
    # defensive quit in case driver is missing or already closed
    if hasattr(context, "driver") and context.driver:
        try:
            context.driver.quit()
            print("Browser closed for scenario")
        except Exception as e:
            print("Error quitting browser:", e)
