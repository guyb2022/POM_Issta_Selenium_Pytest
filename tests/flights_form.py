import pytest
import time
from selenium import webdriver
from pages.flights_form import FLightForm


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


def test_flights_origin(driver):
    flLightform = FLightForm(driver)
    # open the main page
    flLightform.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flLightform.remove_ads()
    # set origin
    actual = flLightform.origin_check()
    assert actual == flLightform.origin
    time.sleep(1)


def test_flights_destination(driver):
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flight_form.remove_ads()
    # set origin
    actual = flight_form.destination_check()
    assert actual == flight_form.destination
    time.sleep(1)


def test_flight_dates(driver):
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flight_form.remove_ads()
    # choose dates
    flight_form.pick_date()
    time.sleep(1)


def test_add_adult_passengers(driver):
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click add adult '+' sign
    flight_form.choose_adult_passenger()
    time.sleep(1)


def test_add_young_passengers_check(driver):
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click add young passenger
    flight_form.choose_child_passenger()
    time.sleep(1)


def test_click_search_wo_parameters(driver):
    # Test behave hen no parameters are picked
    # There are 16 optional cases to check for 4 items.
    # I choose to check the empty case w/o parameters
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page('https://www.issta.co.il/flights')
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click the search button
    flight_form.choose_flight_button()
    assert driver.switch_to.alert.text == "* לא נבחר תאריך יציאה\n* לא נבחר תאריך חזרה\n* נא בחר יעד"


def teardown_method(driver):
    time.sleep(10)
    driver.quit()