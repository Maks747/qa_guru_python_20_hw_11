import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import os

@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()

def browser_settings():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1366
    browser.config.window_height = 705
    browser.config.timeout = 30


    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


