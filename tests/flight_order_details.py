import pytest
import time
from selenium import webdriver
from pages.flight_order_details import FlightOrderDetails


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


def test_order_flight_details_registration(driver):
    # Registration form
    flight_order_passenger_reg = FlightOrderDetails(driver)
    # open the main page
    flight_order_passenger_reg.open_page("https://www.issta.co.il/flights/checkout?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # remove the ads banner if exist
    flight_order_passenger_reg.remove_ads()
    flight_order_passenger_reg.order_flight_passenger_registration()
    time.sleep(1)
    # Checked & Passed


def test_order_flight_passenger_details(driver):
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
    # Checked & Passed


def test_order_flight_additional_services(driver):
    # Services form
    flight_order_additional_service = FlightOrderDetails(driver)
    # open the main page
    flight_order_additional_service.open_page("https://www.issta.co.il/flights/checkout/general_service?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_additional_service.remove_ads()
    flight_order_additional_service.order_flight_services_details()
    time.sleep(1)
    # Checked & Passed


def test_order_flight_order(driver):
    # Order form
    flight_order_order = FlightOrderDetails(driver)
    # open the main page
    flight_order_order.open_page("https://www.issta.co.il/flights/checkout/paymant?seid=f1cd0b50-9b69-4b21-be20-9ab1eaf61834")
    time.sleep(3)
    # Remove the ads banner if exist
    flight_order_order.remove_ads()
    flight_order_order.order_flight_order()
    time.sleep(1)
    # Checked & Passed


def teardown_method(driver):
    time.sleep(10)
    driver.quit()

