import pytest
from selene import browser
from selenium import webdriver
from utils import attach

@pytest.fixture(scope='function')
def setting_browser(request):
    options = webdriver.ChromeOptions()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.driver.maximize_window()


    yield browser
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_screenshot(browser)
    browser.quit()
