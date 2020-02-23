from selenium.webdriver.common.by import By
from automation_site.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccount(BasePage):

    home_page_link_xpath = (By.XPATH, '//*[@title="Return to Home"]')


    order_history_xpath = (By.XPATH, '//a[@title="Orders"]')
    credit_slips = (By.XPATH, '//a[@title="Orders"]')
    my_address_xpath = (By.XPATH, '//a[@title="Addresses"]')
    personal_information_xpath = (By.XPATH, '//a[@title="information"]')
    personal_information_xpath = (By.XPATH, '//a[@title="My wishlists"]')

    def verify_page(self):
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(self.order_history_xpath))
        assert 'My account - My Store' in self.driver.title
    
