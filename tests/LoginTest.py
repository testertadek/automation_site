from BaseTest import BaseTest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from automation_site.pages.HeaderPage import HeaderPage
from automation_site.pages.LoginPage import LoginPage
from automation_site.pages.MyAccount import MyAccount
import unittest
from time import sleep
import csv
from ddt import ddt, data, unpack

# pobieranie danych z pliku
def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt', )
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class LoginTest(BaseTest) :

    @data(*get_data("login.csv"))
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
