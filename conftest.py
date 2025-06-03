from selenium import webdriver
import pytest
from selene import browser
import time
@pytest.fixture(scope='function')
def setting_browser_from_selene():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.wait_until(1000)
    yield
    time.sleep(2)
    browser.quit()