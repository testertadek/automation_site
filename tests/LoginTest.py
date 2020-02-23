import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from automation_site.tests.BaseTest import BaseTest

from automation_site.pages.HeaderPage import HeaderPage
from automation_site.pages.LoginPage import LoginPage
from automation_site.pages.MyAccount import MyAccount
from automation_site.test_utils import utils
import unittest
from time import sleep
import csv
from ddt import ddt, data, unpack
file_path = os.path.join(os.path.dirname(__file__),"..", "test_data/login.csv")

# pobieranie danych z pliku
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

@ddt
class LoginTest(BaseTest) :

    @data(*utils.get_data(file_path))
    @unpack
    def test_good_credentials(self, email, password):
        header = HeaderPage(self.driver)
        header.click_login_link()

        print("TEst jest ok ")
        login_page = LoginPage(self.driver)
        login_page.fill_login_email(email)
        login_page.fill_password(password)
        login_page.click_login_button()
        my_acccount = MyAccount(self.driver)
        my_acccount.verify_page()
        sleep(2)


if __name__ == "__main__":
    unittest.main()
