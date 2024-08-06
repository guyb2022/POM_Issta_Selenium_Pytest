import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FLightForm:

    def __init__(self, driver):
        self.driver = driver
        self.ads_link = (By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        self.flight_origin = (By.XPATH,"//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='בחר מוצא']")
        self.origin = ("תל אביב, שדה תעופה TLV")
        self.flight_destination = (By.XPATH, "//input[@class='ng-field ng-field-autocomplete ng-field-destination' and @placeholder='לאיפה?']")
        self.destination = ("בודפשט, הונגריה")
        self.date = (By.ID, "start_date")
        self.from_date = (By.CSS_SELECTOR, ".real-today > .day-number")
        self.to_date = (By.CSS_SELECTOR, ".month2 tr:nth-child(5) > td:nth-child(2) > .day")
        self.adult_passenger = (By.XPATH,"//div[@class='ng-dropdown ng-main-dropdown ng-dropdown-primary ng-passengers-dropdown']")
        self.click_adult = (By.XPATH, "//button[contains(@class, 'ng-spinner-add')]")
        self.child_passenger = (By.CSS_SELECTOR, ".ng-tns-c18-1 .ng-dropdown-button")
        self.click_child = (By.CSS_SELECTOR, ".ng-tns-c18-1 > .\\36 > .ng-spinner-add")
        self.choose_flight = (By.XPATH, "//button[contains(text(), 'חפשו')]")

    def open_page(self, url):
        self.driver.get(url)

    def remove_ads(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.ads_link))).click()
        except Exception:
            print("No Popup Appeared in here")

    def origin_check(self):
        origin = self.driver.find_element(*self.flight_origin)
        origin.clear()
        origin.send_keys(self.origin)
        return origin.get_attribute('value')

    def destination_check(self):
        destination = self.driver.find_element(*self.flight_destination)
        destination.clear()
        destination.send_keys(self.destination)
        return destination.get_attribute('value')

    def pick_date(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.date)))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.from_date)))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.to_date)))).click()

    def choose_adult_passenger(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.adult_passenger)))).click()
        time.sleep(3)
        # Wait for the "+" button to be visible and then click it
        add_passenger_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.click_adult)))
        add_passenger_button.click()

    def choose_child_passenger(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (self.driver.find_element(*self.child_passenger)))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (self.driver.find_element(*self.click_child)))).click()

    def choose_flight_button(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.choose_flight))).click()
