from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="searchresults_card"]'
        )

    def pull_titles(self):
        deal_box = self.pull_deal_boxes()[0]
        flight_name = (
            deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="flight_card_carrier_0"]'
            )
            .get_attribute("innerHTML")
            .strip()
        )
        flight_price = (
            deal_box.find_element(By.CLASS_NAME, "css-vxcmzt")
            .get_attribute("innerHTML")
            .strip()
        )
        depart_flight = (
            deal_box.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="flight_card_segment_departure_date_0"]',
            )
            .get_attribute("innerHTML")
            .strip()
        )
        return_flight = (
            deal_box.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="flight_card_segment_departure_date_1"]',
            )
            .get_attribute("innerHTML")
            .strip()
        )
        return [flight_name, flight_price, depart_flight, return_flight]
