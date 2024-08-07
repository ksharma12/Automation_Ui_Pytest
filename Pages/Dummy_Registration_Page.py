import time

from selenium.webdriver.common.by import By

import OR
from Selenium_Operations.Element_Operations import Element_Operations


class dummy_registration(Element_Operations):
    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def fill_registration_form(self, name, phoneNumber, email, country, city, username, password):
        self.set_fullscreen_window()
        self.wait_until_element_present_visible(OR.name)
        self.send_keys(OR.name, name)
        self.wait_until_element_present_visible(OR.phone)
        self.send_keys(OR.phone, phoneNumber)
        self.wait_until_element_present_visible(OR.email)
        self.send_keys(OR.email, email)
        self.wait_until_element_present_visible(OR.country)
        self.select_by_value(OR.country, country)
        self.wait_until_element_present_visible(OR.city)
        self.send_keys(OR.city, city)
        self.wait_until_element_present_visible(OR.username)
        self.send_keys(OR.username, username)
        self.wait_until_element_present_visible(OR.password)
        self.send_keys(OR.password, password)
