import allure
from allure_commons._allure import step

from Object_Repository import Resources_OR, Practice_Site_1_OR
from Selenium_Operations.Element_Operations import Element_Operations


class Automation_Practice_Site_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    @allure.step("Verify if user landed on Automation Practice site")
    def Automation_Practice_Site_Window_Title(self):
        Window_Title = self.get_window_title()
        assert Window_Title == "Welcome"

    @allure.step("Enter Draggable page")
    def Enter_Draggable_page(self):
        self.set_fullscreen_window()
        self.wait_until_element_clickable(Practice_Site_1_OR.Draggable_img)
        self.click(Practice_Site_1_OR.Draggable_img)

    @allure.step("Drag and Drop item and check its functionality")
    def Drag_and_Drop(self):
        windows = self.get_window_handles()
        self.switch_to_window(windows[1])
        self.maximize_window()
        self.wait_until_element_present_visible(Practice_Site_1_OR.Default_functionality_iframe)
        frames = self.find_elements(Practice_Site_1_OR.Default_functionality_iframe)
        self.switch_to_frame(frames[0])
        self.drag_and_drop_element_via_offset(Practice_Site_1_OR.Draggable_obj, 1200, 600)
