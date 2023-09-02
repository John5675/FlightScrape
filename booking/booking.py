from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
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

    def select_dates(self, check_in_date, check_out_date):
        search_field = self.find_element(
            By.CSS_SELECTOR, 'button[data-ui-name="button_date_segment_0"]'
        )
        search_field.click()
        check_in_split = check_in_date.split()
        check_out_split = check_out_date.split()
        # print(check_in_split[1])

        while True:
            element = self.find_element(By.CSS_SELECTOR, 'h3[aria-live="polite"]')
            inner_html = element.get_attribute("innerHTML")
            inner_html = inner_html.split()
            print(inner_html[0])
            next_button = self.find_element(
                By.CLASS_NAME, "Calendar-module__control--next___C2mkG"
            )
            if inner_html[0] != check_in_split[1]:
                next_button.click()
            if inner_html[0] == check_in_split[1]:
                break

        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[aria-label="{check_in_date}"]'
        )
        check_in_element.click()

        while True:
            element = self.find_element(By.CSS_SELECTOR, 'h3[aria-live="polite"]')
            inner_html = element.get_attribute("innerHTML")
            inner_html = inner_html.split()
            print(inner_html[0])
            next_button = self.find_element(
                By.CLASS_NAME, "Calendar-module__control--next___C2mkG"
            )
            if inner_html[0] != check_out_split[1]:
                next_button.click()
            if inner_html[0] == check_out_split[1]:
                break

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[aria-label="{check_out_date}"]'
        )
        check_out_element.click()

    def search_button(self):
        element = self.find_element(
            By.CSS_SELECTOR, 'button[data-ui-name="button_search_submit"]'
        )
        element.click()
