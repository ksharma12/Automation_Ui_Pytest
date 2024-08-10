import allure

from Object_Repository import Dummy_Registration_Form_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Dummy_Registration_Page(Element_Operations):
    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def fill_registration_form(self, name, phoneNumber, email, country, city, username, password):
        self.set_fullscreen_window()
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.name)
        self.send_keys(Dummy_Registration_Form_OR.name, name)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.phone)
        self.send_keys(Dummy_Registration_Form_OR.phone, phoneNumber)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.email)
        self.send_keys(Dummy_Registration_Form_OR.email, email)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.country)
        self.select_by_value(Dummy_Registration_Form_OR.country, country)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.city)
        self.send_keys(Dummy_Registration_Form_OR.city, city)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.username)
        self.send_keys(Dummy_Registration_Form_OR.username, username)
        self.wait_until_element_present_visible(Dummy_Registration_Form_OR.password)
        self.send_keys(Dummy_Registration_Form_OR.password, password)

    def enter_to_the_testing_website(self):
        self.click(Dummy_Registration_Form_OR.ENTER_TO_THE_TESTING_WEBSITE)
