import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    # Init driver with options and yeild driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver


def test_flights_page(driver):
    # Test the Home PAge website
    driver.get('https://www.issta.co.il/')
    # Closing popups
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')))).click()
    except Exception:
        print("No Popup Appeared in here")
    # Press the flights button/link
    flights_page = driver.find_element(By.XPATH,
                                      "//a[@class='nav-link dropdown-toggle' and @data-target='#section2']")
    flights_page.click()
    # get the header text
    page_header = driver.title
    time.sleep(3)
    # compare the actual header and the desired headr
    assert page_header == 'טיסות - טיסות זולות - השוואת מחירי טיסות לחול | איסתא'


def test_flights_origin(driver):
    driver.get('https://www.issta.co.il/flights')
    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    search_origin = driver.find_element(By.XPATH,"//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='בחר מוצא']")
    search_origin.clear()
    search_origin.send_keys("אמסטרדם, הולנד")
    actual = search_origin.get_attribute('value')
    assert actual == "אמסטרדם, הולנד"
    time.sleep(3)

def test_flights_destination(driver):
    driver.get('https://www.issta.co.il/flights')
    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    search_destination = driver.find_element(By.XPATH,
                                             "//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='לאיפה?']")
    search_destination.clear()
    search_destination.send_keys("בודפשט, הונגריה")
    actual = search_destination.get_attribute('value')
    assert actual == "בודפשט, הונגריה"
    time.sleep(3)


def test_flight_dates(driver):
    driver.get('https://www.issta.co.il/flights')
    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    # Choose date
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.ID, "start_date")))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                                                             ".real-today > .day-number")))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                                                             ".month2 tr:nth-child(5) > td:nth-child(2) > .day")))).click()
    time.sleep(3)


def test_add_adult_passengers(driver):
    driver.get('https://www.issta.co.il/flights')
    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,"//div[@class='ng-dropdown ng-main-dropdown ng-dropdown-primary ng-passengers-dropdown']")))).click()
    time.sleep(3)
    # Wait for the "+" button to be visible and then click it
    add_passenger_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ng-spinner-add')]"))
    )
    add_passenger_button.click()
    time.sleep(3)


def test_add_young_passengers_check(driver):
    driver.get('https://www.issta.co.il/flights')
    driver.maximize_window()
    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.CSS_SELECTOR, ".ng-tns-c18-1 .ng-dropdown-button")))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.CSS_SELECTOR, ".ng-tns-c18-1 > .\\36 > .ng-spinner-add")))).click()
    time.sleep(3)

def test_search_button_wo_all_parameters(driver):
    driver.get('https://www.issta.co.il/flights')
    driver.maximize_window()

    # Closing popups
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[contains(text(), 'חפשו')]"))))
    element.click()
    time.sleep(3)
    assert driver.switch_to.alert.text == "* לא נבחר תאריך יציאה\n* לא נבחר תאריך חזרה\n* נא בחר יעד"


def test_order_flight(driver):
    driver.get("https://www.issta.co.il/flights/results.aspx?fdate=01/09/24&tdate=11/09/24&route=2&dport=TLV&aport=AMS&padt=1")
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    number_of_flights = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//span[@id='number_of_results']")))).text
    if int(number_of_flights) > 0:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((driver.find_element(By.LINK_TEXT, "פרטי טיסה")))).click()
    time.sleep(3)

def test_order_flight_details(driver):

    driver.get("https://www.issta.co.il/flights/details.aspx?sourceid=1717&flightnumbers=1302;1093;512&airline=UX,IZ&fdate=01/09/24&tdate=11/09/24&route=2&dport=TLV&aport=AMS&padt=1&fid=521&seid=638583970997072481")
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    order_details = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[@class='btn btn-block btn-primary']")))).click()

    time.sleep(3)

def test_order_flight_details_registration(driver):
    driver.get("https://www.issta.co.il/flights/checkout?seid=4312195d-e5f3-439c-962d-1b94956561cf")
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    first_name = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='checkout-first-name']"))))
    first_name.clear()
    first_name.send_keys('Mr. Smith')

    last_name = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='checkout-last-name']"))))
    last_name.clear()
    last_name.send_keys('smith')

    email = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='checkout-email']"))))
    email.clear()
    email.send_keys('mrsmith@smith.co.il')

    phone = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='checkout-phone']"))))
    phone.clear()
    phone.send_keys('053-5587789')

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".checkout-step__body")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".btn")))).click()

    time.sleep(10)


def test_passenger_details(driver):
    driver.get("https://www.issta.co.il/flights/checkout/personal_detailes?seid=a1faa362-65d1-43e5-8ef7-810cdb3f3a9b")
    # driver.set_window_size(1936, 1168)
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[@id='_ZAbanner_CLOSE_BUTTON']")))).click()


    first_name = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='PassengerDetailsVM.PassengersVM.Passengers[0].FirstName']"))))
    first_name.clear()
    first_name.send_keys('Mr. Smith')

    last_name = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//input[@id='PassengerDetailsVM.PassengersVM.Passengers[0].LastName']"))))
    last_name.clear()
    last_name.send_keys('Smith')

    time.sleep(3)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH, "//div[@class='selectric']")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".selectric-scroll li:nth-child(2)")))).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.ID, "PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.ID, "PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate")))).send_keys("20/06/1976")

    time.sleep(1)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".outbound .baggage-selector-option-upper-section:nth-child(1) > .upper-section-text")))).click()

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                             ".baggage-area-selecting:nth-child(10) .baggage-selector-option:nth-child(2) > .baggage-selector-option-lower-section")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                             ".baggage-area-selecting:nth-child(7) .selected-option .upper-section-icon")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                                                        ".baggage-area-selecting:nth-child(12) .baggage-selector-option:nth-child(2) > .baggage-selector-option-lower-section")))).click()
    driver.execute_script("window.scrollTo(0, 500)")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[contains(@class,'btn btn--default step-one-submit')]")))).click()

    time.sleep(3)


def test_additional_services(driver):
    driver.get("https://www.issta.co.il/flights/checkout/general_service?seid=23764ae8-3bb0-4f1a-996b-8ab130ccf116")
    # driver.set_window_size(1936, 1168)
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[@id='_ZAbanner_CLOSE_BUTTON']")))).click()
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.ID, "FLX - Flight horizon up to 35, $900, $39 VIP-4")))).click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.ID, "Trip Shield-4")))).click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.ID, "CityRide-4")))).click()
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(3)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (driver.find_element(By.XPATH, "//button[contains(text(), 'המשיכו')]")))).click()
    time.sleep(3)


def test_payment(driver):
    driver.get("https://www.issta.co.il/flights/checkout/paymant?seid=23764ae8-3bb0-4f1a-996b-8ab130ccf116")
    # driver.set_window_size(1936, 1168)
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    # close the "chrome is been controlled by..."
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                        "//button[@id='_ZAbanner_CLOSE_BUTTON']")))).click()
    driver.execute_script("window.scrollTo(0, 200)")
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".payment-check")))).click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR, ".payment-btn")))).click()
    time.sleep(3)


def test_search_button_success(driver):
    vars = {}
    driver.get('https://www.issta.co.il/flights')
    driver.maximize_window()

    # Closing popups if appeared
    try:
        close_popup = driver.find_element(By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        close_popup.click()
    except Exception:
        print("No Popup Appeared in here")

    # Choose Origin
    search_origin = driver.find_element(By.XPATH,
                                        "//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='בחר מוצא']")
    search_origin.clear()
    search_origin.send_keys("תל אביב, שדה תעופה TLV")
    time.sleep(1)
    # Choose Destination
    search_destination = driver.find_element(By.XPATH,
                                             "//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='לאיפה?']")
    search_destination.clear()
    search_destination.send_keys("ברצלונה, ספרד")
    time.sleep(1)

    # Choose date
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.ID, "start_date")))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                                                             ".real-today > .day-number")))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((driver.find_element(By.CSS_SELECTOR,
                                                        ".month2 tr:nth-child(5) > td:nth-child(2) > .day")))).click()

    # Add passenger (Failed here but work well separately)
    # time.sleep(3)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((driver.find_element(By.XPATH,"//div[@class='ng-dropdown ng-main-dropdown ng-dropdown-primary ng-passengers-dropdown']")))).click()
    # # Wait for the "+" button to be visible and then click it
    # add_passenger_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ng-spinner-add')]"))
    # )
    # add_passenger_button.click()

    time.sleep(3)

    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                             "//button[contains(text(), 'חפשו')]"))))
    element.click()
    time.sleep(30)
    number_of_flights = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((driver.find_element(By.XPATH,
                                                            "//span[@id='number_of_results']")))).text
    print("number_of_flights: ",number_of_flights)


def teardown_method(driver):
    time.sleep(10)
    driver.quit()
