from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
import os
import time


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"SeleniumDrivers", teardown=False):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def dismiss_sign_in_pop_up(self):
        try:
            dismiss_button = WebDriverWait(self).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
                )
            )
            dismiss_button.click()
        except:
            print("Sign-in pop-up did not appear or was already closed.")

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.dismiss_sign_in_pop_up()

    def select_airport(self, place_to_go):
        search_field = self.find_element(
            By.CSS_SELECTOR, 'button[data-ui-name="input_location_to_segment_0"]'
        )
        search_field.click()
        input_field = self.find_element(
            By.CSS_SELECTOR, 'input[placeholder="Airport or city"]'
        )
        input_field.click()
        input_field.send_keys(place_to_go)

        airport = self.find_element(
            By.CSS_SELECTOR, f'input[name="AIRPORT{place_to_go}"]'
        )

        airport.click()
