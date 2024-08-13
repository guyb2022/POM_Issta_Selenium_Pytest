from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FlightDetails:

    def __init__(self, driver):
        self.driver = driver
        self.ads_link = (By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')
        self.flight_details = (By.XPATH, "//button[@class='btn btn-block btn-primary']")

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def remove_ads(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.ads_link))).click()
        except Exception:
            print("No Popup Appeared in here")

    def proceed_to_flights_details(self):
        # The button is on the far edge of the screen, cannot be detected
        self.driver.execute_script("window.scrollTo(0, 300)")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.flight_details)))).click()
