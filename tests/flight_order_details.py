import pytest
import time
from pages.flight_order_details import FlightOrderDetails


@pytest.mark.resgression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_details_registration(initialize_driver):
    driver = initialize_driver
    # Registration form
    flight_order_passenger_reg = FlightOrderDetails(driver)
    # open the main page
    flight_order_passenger_reg.open_page("https://www.issta.co.il/flights/checkout?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # remove the ads banner if exist
    flight_order_passenger_reg.remove_ads()
    flight_order_passenger_reg.order_flight_passenger_registration()
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_passenger_details(initialize_driver):
    driver = initialize_driver
    # Fill th passenger details
    flight_order_passenger_details = FlightOrderDetails(driver)
    # open the main page
    flight_order_passenger_details.open_page(
        "https://www.issta.co.il/flights/checkout/personal_detailes?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_passenger_details.remove_ads()
    flight_order_passenger_details.order_flight_passenger_details()
    time.sleep(1)


@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_additional_services(initialize_driver):
    driver = initialize_driver
    # Services form
    flight_order_additional_service = FlightOrderDetails(driver)
    # open the main page
    flight_order_additional_service.open_page("https://www.issta.co.il/flights/checkout/general_service?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_additional_service.remove_ads()
    flight_order_additional_service.order_flight_services_details()
    time.sleep(1)


@pytest.mark.usefixtures('initialize_driver')
def test_order_flight_order(initialize_driver):
    driver = initialize_driver
    # Order form
    flight_order_order = FlightOrderDetails(driver)
    # open the main page
    flight_order_order.open_page("https://www.issta.co.il/flights/checkout/paymant?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_order.remove_ads()
    flight_order_order.order_flight_order()
    time.sleep(1)


