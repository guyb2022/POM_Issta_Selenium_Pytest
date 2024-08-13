import pytest
import time
from pages.flight_available_list import FlightList
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flights_list_details(initialize_driver):
    driver = initialize_driver
    # Available All Flights List
    flight_list = FlightList(driver)
    # open the main page
    flight_list.open_page(os.getenv("URL_FLIGHT_AVAILABLE_LIST"))
    time.sleep(3)
    # remove the ads banner if exist
    flight_list.remove_ads()
    # get the actual flight available
    flight_list.choose_flight()
    time.sleep(3)
    page_header = driver.title
    assert page_header == "תוצאות חיפוש מחירי טיסות מתל אביב לאמסטרדם: 01/09/2024 - 11/09/2024 | איסתא"
