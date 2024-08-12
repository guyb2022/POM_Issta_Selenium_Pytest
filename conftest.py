import pytest
from selenium import webdriver

"""
This file holds all tests vars to be used by all functions
 It can hols class/ fixtures/ function etc.
"""


@pytest.fixture()
def initialize_driver():
    # Init driver with options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()


