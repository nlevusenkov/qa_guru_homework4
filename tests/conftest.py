import pytest
from selenium import webdriver
from selene import Browser, Config


@pytest.fixture(scope='function')
def setting_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }
    options.set_capability("selenoid:options", capabilities["selenoid:options"])

    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver=driver,
                             base_url='https://demoqa.com/automation-practice-form',
                             window_width=1920,
                             window_height=1080))

    yield browser
    browser.quit()
