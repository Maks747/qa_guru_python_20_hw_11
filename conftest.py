import pytest
from selene import browser
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import os

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    #browser.config.timeout = 50
    browser.config.driver.maximize_window()
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


