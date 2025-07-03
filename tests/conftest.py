import pytest
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setting_browser():
    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {"enableVideo": False})

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser_driver = Browser(Config(
        driver=driver,
        window_width=1920,
        window_height=1329,
    ))

    yield browser_driver

    browser_driver.quit()
