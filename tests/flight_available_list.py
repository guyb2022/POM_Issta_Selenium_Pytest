import pytest
import time
from selenium import webdriver
from pages.flight_available_list import FlightList


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


def test_flights_list_details(driver):
    # Available All Flights List
    flight_list = FlightList(driver)
    # open the main page
    flight_list.open_page("https://www.issta.co.il/flights/results.aspx?fdate=01/09/24&tdate=11/09/24&route=2&dport=TLV&aport=AMS&padt=1")
    time.sleep(3)
    # remove the ads banner if exist
    flight_list.remove_ads()
    # get the actual flight available
    flight_list.choose_flight()
    time.sleep(3)
    page_header = driver.title
    assert page_header == "תוצאות חיפוש מחירי טיסות מתל אביב לאמסטרדם: 01/09/2024 - 11/09/2024 | איסתא"


def teardown_method(driver):
    time.sleep(10)
    driver.quit()