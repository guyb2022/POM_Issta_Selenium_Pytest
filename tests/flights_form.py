import pytest
import time
from Pages.flights_form import FLightForm
import os
from dotenv import load_dotenv

load_dotenv()


# @pytest.mark.skip
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flights_origin(initialize_driver):
    driver = initialize_driver
    flightform = FLightForm(driver)
    # open the main page
    flightform.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flightform.remove_ads()
    # set origin
    actual = flightform.origin_check()
    assert actual == flightform.origin
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flights_destination(initialize_driver):
    driver = initialize_driver
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flight_form.remove_ads()
    # set origin
    actual = flight_form.destination_check()
    assert actual == flight_form.destination
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flight_dates(initialize_driver):
    driver = initialize_driver
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flight_form.remove_ads()
    # choose dates
    flight_form.pick_date()
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_add_adult_passengers(initialize_driver):
    driver = initialize_driver
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click add adult '+' sign
    flight_form.choose_adult_passenger()
    time.sleep(1)


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_add_young_passengers_check(initialize_driver):
    driver = initialize_driver
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click add young passenger
    flight_form.choose_child_passenger()
    time.sleep(1)


@pytest.mark.skip(reason="Hebrew/English syntax comparison cannot be matched for exception check")
@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_click_search_wo_parameters(initialize_driver):
    driver = initialize_driver
    # Test behave with no parameters are picked
    # There are 16 optional cases to check for 4 items.
    # I choose to check the empty case w/o parameters
    flight_form = FLightForm(driver)
    # open the main page
    flight_form.open_page(os.getenv("URL_FLIGHT_FORM"))
    # remove the ads banner if exist
    flight_form.remove_ads()
    # click the search button
    flight_form.choose_flight_button()
    time.sleep(3)
    expected = "* לא נבחר תאריך יציאה* לא נבחר תאריך חזרה* נא בחר יעד"
    assert driver.switch_to.alert.text == expected