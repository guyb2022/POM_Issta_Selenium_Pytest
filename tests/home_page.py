import pytest
import time
from selenium import webdriver
from pages.home_page import HomePage


@pytest.fixture()
def driver():
    # Init driver with options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver


def test_issta_home_page_flights(driver):
    home_page = HomePage(driver)
    # open the main page
    home_page.open_page('https://www.issta.co.il/')
    # remove the ads banner if exist
    home_page.remove_ads()
    # click on the flights link
    home_page.click_on_flights_link()
    time.sleep(3)
    # Get the page title
    page_header = driver.title
    # compare the actual header and the desired header
    assert page_header == 'טיסות - טיסות זולות - השוואת מחירי טיסות לחול | איסתא'


def teardown_method(driver):
    time.sleep(10)
    driver.quit()