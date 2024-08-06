import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ChooseFlight:

    def __init__(self, driver):
        self.driver = driver
        self.number_of_flights = (By.XPATH, "//span[@id='number_of_results']")
        self.ads_link = (By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        self.flight_button = (By.LINK_TEXT, "פרטי טיסה")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def remove_ads(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.ads_link))).click()
        except Exception:
            print("No Popup Appeared in here")

    def choose_flight(self):
        number_of_flights = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.number_of_flights))).text
        if int(number_of_flights) > 0:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.flight_button))).click()
        else:
            print("No Flights are Available")