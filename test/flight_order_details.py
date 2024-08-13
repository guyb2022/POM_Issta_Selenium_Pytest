import pytest
import time
from pages.flight_order_details import FlightOrderDetails
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


# @pytest.mark.skip
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_details_registration(initialize_driver):
    driver = initialize_driver
    # Registration form
    flight_order_passenger_reg = FlightOrderDetails(driver)
    # open the main page
    flight_order_passenger_reg.open_page(os.getenv("URL_FLIGHT_ORDER_DETAILS"))
    time.sleep(3)
    # remove the ads banner if exist
    flight_order_passenger_reg.remove_ads()
    flight_order_passenger_reg.order_flight_passenger_registration()
    time.sleep(1)


# @pytest.mark.skip
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_passenger_details(initialize_driver):
    driver = initialize_driver
    # Fill th passenger details
    flight_order_passenger_details = FlightOrderDetails(driver)
    # open the main page
    flight_order_passenger_details.open_page(os.getenv("URL_FLIGHT_ORDER_DETAILS_PERSONAL_DETAILS"))
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_passenger_details.remove_ads()
    flight_order_passenger_details.order_flight_passenger_details()
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_additional_services(initialize_driver):
    driver = initialize_driver
    # Services form
    flight_order_additional_service = FlightOrderDetails(driver)
    # open the main page
    flight_order_additional_service.open_page(os.getenv("URL_FLIGHT_ORDER_DETAILS_GENERAL_SERVICE"))
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_additional_service.remove_ads()
    flight_order_additional_service.order_flight_services_details()
    time.sleep(1)


# @pytest.mark.skip
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_order(initialize_driver):
    driver = initialize_driver
    # Order form
    flight_order_order = FlightOrderDetails(driver)
    # open the main page
    flight_order_order.open_page(os.getenv("URL_FLIGHT_ORDER_DETAILS_PAYMENT"))
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_order.remove_ads()
    flight_order_order.order_flight_order()
    time.sleep(1)


