import pytest
import time
from pages.flight_details import FlightDetails


@pytest.mark.regression
@pytest.mark.usefixtures('initialize_driver')
def test_flight_details(initialize_driver):
    driver = initialize_driver
    print("Staring test for flight details page")
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
    print("End test for flight details page")
