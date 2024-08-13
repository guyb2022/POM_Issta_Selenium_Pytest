import pytest
import time
from pages.flight_details import FlightDetails
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flight_details(initialize_driver):
    driver = initialize_driver
    print("Staring test for flight details page")
    # Available All Flights List
    flight_details = FlightDetails(driver)
    # open the main page
    flight_details.open_page(os.getenv("URL_FLIGHT_DETAILS"))
    time.sleep(3)
    # remove the ads banner if exist
    flight_details.remove_ads()
    flight_details.proceed_to_flights_details()
    page_header = driver.title
    time.sleep(3)
    assert page_header == "אישור פרטי הזמנה | איסתא"
    print("End test for flight details page")
