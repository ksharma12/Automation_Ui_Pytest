import allure

from Object_Repository import Resources_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Automation_Practice_Site_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    allure.step("Getting Automation Practice Site Window Title ")

    def Automation_Practice_Site_Window_Title(self):
        Window_Title = self.get_window_title()
        print(Window_Title)
