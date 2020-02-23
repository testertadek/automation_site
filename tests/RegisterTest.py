import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from automation_site.tests.BaseTest import BaseTest
from automation_site.pages.HeaderPage import HeaderPage
from automation_site.pages.LoginPage import LoginPage
from automation_site.pages.RegisterPage import RegisterPage

import unittest
from time import sleep



class RegisterTest(BaseTest) :
    reg_data = {'email': 'data23@data.com', 'gender':'male', 'first_name':'Tadek', 'last_name': 'Testowiak', 'password' : 'qwer4321'}

    def test_invalid_postcode(self):
        #header part
        header = HeaderPage(self.driver)
        header.click_login_link()
        #login page part
        login_page = LoginPage(self.driver)
        login_page.fill_register_email(self.reg_data['email'])
        login_page.click_register_button()
        # registration page part
        reg_page = RegisterPage(self.driver)
        reg_page.choose_gender(self.reg_data['gender'])

        #added just to see final state of test, sleep will be remove
        sleep(3)
        #to do finish RegisterTEst

if __name__ == "__main__":
    unittest.main()
