from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
import os


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

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[class="a83ed08757 aee4999c52 ffc914f84a c39dd9701b ac7953442b abced745f1"]',
        )
        selected_currency_element.click()
