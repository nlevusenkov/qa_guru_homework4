import pytest
from selenium import webdriver
from selene import Browser, Config


@pytest.fixture(scope='function')
def setting_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    capabilities = {
        "browserVersion": "128.0",
        "browserName": "chrome",
        "selenoid:options": {
            "enableVideo": False
        }
    }
    options.set_capability("selenoid:options", capabilities["selenoid:options"])

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Создание браузера с нужной конфигурацией
    browser = Browser(Config(
        driver=driver,
        window_width=1920,
        window_height=1080,
    ))

    yield browser
    browser.quit()
