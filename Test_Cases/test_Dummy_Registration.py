import pytest
import logging
from Pages.Dummy_Registration_Page import Dummy_Registration_Page
from Pages.Home_Page import Home_Page
from Pages.Selenium_4_Popup_Page import Selenium_4_Popup_Page
from Test_Cases.BaseTest import BaseTest
from Utils import dataProvider
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Test_Dummy_Registration(BaseTest):

    @pytest.mark.parametrize("name, phoneNum, email, country, city, username, password",
                             dataProvider.get_data("LoginTest"))
    @pytest.mark.regression
    def test_doSignUp(self, name, phoneNum, email, country, city, username, password):
        Selenium4PopUpPage = Selenium_4_Popup_Page(self.driver)
        home = Home_Page(self.driver)
        dummy_reg = Dummy_Registration_Page(self.driver)
        Selenium4PopUpPage.close_selenium_four_popup()
        home.moving_to_Dummy_Registration_Page()
        dummy_reg.fill_registration_form(name, phoneNum, email, country, city, username, password)






