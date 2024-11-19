from selene import browser
from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def setting():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_height = 2560
    browser.config.window_width = 1440
    browser.open('https://google.com/ncr')
    browser.config.timeout = 20

    yield

    browser.quit()
