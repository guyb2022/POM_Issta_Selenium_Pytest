from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.flight_link = (By.XPATH, "//a[@class='nav-link dropdown-toggle' and @data-target='#section2']")
        self.ads_link = (By.ID, 'ZA_CAMP_CLOSE_BUTTON_CONTAINER')

    def open_page(self, url):
        self.driver.get(url)

    def remove_ads(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.ads_link))).click()
        except Exception:
            print("No Popup Appeared in here")

    def click_on_flights_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(*self.flight_link)))).click()



