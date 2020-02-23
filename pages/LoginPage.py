from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from automation_site.pages.BasePage import BasePage

class LoginPage(BasePage):

    home_page_link_xpath        =  (By.XPATH, '//*[@title="Return to Home"]')

    #create accoutn box
    register_email_xpath        = (By.XPATH, '//*[@id = "email_create"]')
    register_button_xpath       = (By.XPATH, '//*[@id="SubmitCreate"]')

    #Login (already register box)
    email_login_input_xpath     = (By.XPATH, '//*[@id = "email"]')
    password_input_xpath        = (By.XPATH, '//*[@id = "passwd"]')
    reset_passwrod_link_xpath   = (By.XPATH, '//*[@title="Recover your forgotten password"]')
    login_button_xpath          = (By.XPATH, '//*[@id = "SubmitLogin"]')

    email = 'data21@data.com'
    login_password = 'abcd1234'


    def fill_register_email(self, email):
        email_registrer = self.driver.find_element(*self.register_email_xpath)
        email_registrer.send_keys(email)

    def click_register_button(self):
        register_button = self.driver.find_element(*self.register_button_xpath)
        register_button.click()

    def fill_login_email(self, email):
        login_email = self.driver.find_element(*self.email_login_input_xpath)
        login_email.send_keys(email)

    def fill_password(self, password):
        passw_input = self.driver.find_element(*self.password_input_xpath)
        passw_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button_xpath)
        login_button.click()
