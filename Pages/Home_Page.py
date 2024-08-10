import allure

from Object_Repository import Resources_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Home_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    allure.step("Moving to dummy registration page")

    def moving_to_Dummy_Registration_Page(self):
        self.wait_until_element_present_visible(Resources_OR.resources)
        self.move_to_element(Resources_OR.resources).perform_after_actionChains()
        self.wait_until_element_present_visible(Resources_OR.resources_practice_site_1)
        self.click(Resources_OR.resources_practice_site_1)
