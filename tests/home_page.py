import pytest
import time
from pages.home_page import HomePage
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_issta_home_page_flights(initialize_driver):
    driver = initialize_driver
    home_page = HomePage(driver)
    # open the main page
    home_page.open_page(os.getenv("URL_BASE"))
    # remove the ads banner if exist
    home_page.remove_ads()
    # click on the flights link
    home_page.click_on_flights_link()
    time.sleep(3)
    # Get the page title
    page_header = driver.title
    # compare the actual header and the desired header
    assert page_header == 'טיסות - טיסות זולות - השוואת מחירי טיסות לחול | איסתא'
