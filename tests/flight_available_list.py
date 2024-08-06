import pytest
import time
from selenium import webdriver
from pages.choose_flight import ChooseFlight


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


def test_flight_details(driver):
    # Available All Flights List
    flight_details = ChooseFlight(driver)
    # open the main page
    flight_details.open_page("https://www.issta.co.il/flights/results.aspx?fdate=01/09/24&tdate=11/09/24&route=2&dport=TLV&aport=AMS&padt=1")
    # remove the ads banner if exist
    flight_details.remove_ads()
    # get the actual flight available
    flight_details.choose_flight()
    time.sleep(1)

