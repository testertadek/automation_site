import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def tearDwon(self):
        self.driver.quit()

if  __name__ == '__main__' :
    unittest.main()
