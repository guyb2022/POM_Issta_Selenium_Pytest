import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FlightOrderDetails:

    def __init__(self, driver):
        self.driver = driver
        self.pop_up = (By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        self.banner = (By.XPATH, "//button[@id='_ZAbanner_CLOSE_BUTTON']")
        self.first_name_registration = (By.XPATH, "//input[@id='checkout-first-name']")
        self.last_name_registration = (By.XPATH, "//input[@id='checkout-last-name']")
        self.email_registration = (By.XPATH, "//input[@id='checkout-email']")
        self.phone_registration = (By.XPATH, "//input[@id='checkout-phone']")
        self.checkout_registration = (By.CSS_SELECTOR, ".checkout-step__body")
        self.button_registration = (By.CSS_SELECTOR, ".btn")
        self.phone_number = '054-2772399'
        self.email_details = 'abc@gmail.com'
        self.f_name = 'Mr. Jon'
        self.l_name = 'loong'
        self.birth_date = "13/09/1993"
        self.first_name_details = (By.ID, "PassengerDetailsVM.PassengersVM.Passengers[0].FirstName")
        self.last_name_details = (By.XPATH, "//input[@id='PassengerDetailsVM.PassengersVM.Passengers[0].LastName']")
        self.gender_details_click = (By.XPATH, "//div[@class='selectric']")
        self.gender_details = (By.CSS_SELECTOR, ".selectric-scroll li:nth-child(2)")
        self.birthday_click = (By.ID, "PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate")
        self.birthday_set = (By.ID, "PassengerDetailsVM.PassengersVM.Passengers[0].Birthdate")
        self.hand_luggage_forth = (By.CSS_SELECTOR, ".selected-option .upper-section-text")
        self.plain_luggage_forth = (By.CSS_SELECTOR,".baggage-selector-option-lower-section:nth-child(2)")
        self.hand_luggage_back = (By.CSS_SELECTOR, ".baggage-area-selecting:nth-child(7) .selected-option .upper-section-icon")
        self.plain_luggage_back = (By.CSS_SELECTOR, ".baggage-area-selecting:nth-child(12) .baggage-selector-option:nth-child(2) > .baggage-selector-option-lower-section")
        self.button_details = (By.XPATH, "//button[contains(@class,'btn btn--default step-one-submit')]")
        self.vip_radio_button = (By.ID, "FLX - Flight long horizon $50 VIP-4")
        self.quite_radio_button = (By.ID, "Trip Shield-4")
        self.city_ride_radio_button = (By.ID, "CityRide-4")
        self.cont_button =(By.XPATH, "//button[contains(text(), 'המשיכו')]")
        self.proceed_payment = (By.CSS_SELECTOR, ".payment-check")
        self.place_order = (By.CSS_SELECTOR, ".payment-btn")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def remove_ads(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.pop_up))).click()
        except Exception:
            print("No Popup Appeared in here")

    def order_flight_passenger_registration(self):
        first_name = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.first_name_registration)))
        first_name.clear()
        first_name.send_keys(self.f_name)
        last_name = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.last_name_registration)))
        last_name.clear()
        last_name.send_keys(self.l_name)
        email = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.email_registration)))
        email.clear()
        email.send_keys(self.email_details)
        phone = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.phone_registration)))
        phone.clear()
        phone.send_keys(self.phone_number)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.checkout_registration)))).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.button_registration)))).click()

    def order_flight_passenger_details(self):
        # close the "chrome is been controlled by..."
        WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.banner))).click()
        # Set first name
        time.sleep(1)
        first_name = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.first_name_details)))
        first_name.clear()
        first_name.send_keys(*self.f_name)
        # Set last name
        last_name = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.last_name_details)))
        last_name.clear()
        last_name.send_keys(self.l_name)
        time.sleep(3)
        # Set gender
        WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.gender_details_click))).click()
        WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.gender_details))).click()
        # Set birthday
        # Buggy and cause the app to fail WIP
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.birthday_click)))).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.birthday_set)))).send_keys(self.birth_date)
        time.sleep(3)
        # Choose luggage
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.hand_luggage_forth))).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.plain_luggage_forth))).click()
        try:
            # Some flight don't have this option but the same option for both sides of flight
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.hand_luggage_back))).click()
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.plain_luggage_back))).click()
        except Exception:
            print("This option is not available on this flight")
        # The button is on the far edge of the screen, cannot be detected
        self.driver.execute_script("window.scrollTo(0, 500)")
        # push the continue button
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.button_details))).click()
        time.sleep(10)

    def order_flight_services_details(self):
        # close the "chrome is been controlled by..."
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.banner)))).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.vip_radio_button)))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.quite_radio_button)))).click()
        time.sleep(3)
        try:
            # Some flights don't include this option
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((
                    self.driver.find_element(*self.city_ride_radio_button)))).click()
        except Exception:
            "This option is not available on this flight"

        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.cont_button)))).click()
        time.sleep(3)

        actual = self.driver.title
        expected = "אישור פרטי הזמנה | איסתא"
        assert actual == expected

    def order_flight_order(self):
        # close the "chrome is been controlled by..."
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.banner)))).click()
        self.driver.execute_script("window.scrollTo(0, 200)")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.proceed_payment)))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((
                self.driver.find_element(*self.place_order)))).click()
        time.sleep(10)