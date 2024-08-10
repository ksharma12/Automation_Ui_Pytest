import allure

from Object_Repository import Resources_OR, Practice_Site_1_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Automation_Practice_Site_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    allure.step("Getting Automation Practice Site Window Title ")

    def Automation_Practice_Site_Window_Title(self):
        Window_Title = self.get_window_title()
        assert Window_Title == "Welcome"

    allure.step("Entering Draggable page")

    def Enter_Draggable_page(self):
        self.set_fullscreen_window()
        self.click(Practice_Site_1_OR.Draggable_img)

    allure.step("Getting window handles")

    def Drag_and_Drop(self):
        windows = self.get_window_handles()
        self.switch_to_window(windows[1])
        self.switch_to_frame(Practice_Site_1_OR.Default_functionality_iframe)
        #self.drag_and_drop_element_via_offset(Practice_Site_1_OR.Draggable_obj, 120, 120)


