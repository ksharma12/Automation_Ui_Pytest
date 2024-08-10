from Object_Repository import Dummy_Registration_Form_OR
from Selenium_Operations.Element_Operations import Element_Operations


class dummy_registration(Element_Operations):
    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def _registration_form(self):
        self.set_fullscreen_window()
