import pytest
import time
from selenium import webdriver
from pages.flight_details import FlightDetails


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
    flight_details = FlightDetails(driver)
    # open the main page
    flight_details.open_page("https://www.issta.co.il/flights/details.aspx?sourceid=1717&flightnumbers=1302;1093;512&airline=UX,IZ&fdate=01/09/24&tdate=11/09/24&route=2&dport=TLV&aport=AMS&padt=1&fid=551&seid=638584937318127905")
    time.sleep(3)
    # remove the ads banner if exist
    flight_details.remove_ads()
    flight_details.proceed_to_flights_details()
    page_header = driver.title
    time.sleep(3)
    assert page_header == "אישור פרטי הזמנה | איסתא"


def teardown_method(driver):
    time.sleep(10)
    driver.quit()