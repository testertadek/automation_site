from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from automation_site.pages.BasePage import BasePage





class RegisterPage(BasePage):

    #personal information
    male_radio_xpath = (By.XPATH, '//*[@id="id_gender1"]')
    female_radio_xpath = (By.XPATH, '//*[@id="id_gender2"]')
    first_name_input_xpath = (By.XPATH, '//*[@id = "customer_firstname"]')
    last_name_input_xpath = (By.XPATH, '//*[@id = "customer_lastname"]')
    email_input_xpath = (By.XPATH, '//*[@id="email"]')
    password_input_xpath = (By.XPATH, '//*[@id = "passwd"]')


    submit_button_xpath = (By.XPATH, '//*[@id = "submitAccount"]')


    def choose_gender(self, gender):
        if gender == 'male':
            self.driver.find_element(*self.male_radio_xpath).click()
        else:
            self.driver.find_element(*self.female_radio_xpath).click()

    def fill_first_name(self, first_name):
        first_name_input = self.driver.find_element(*self.first_name_input_xpath)
        first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name):
        last_name_input = self.driver.find_element(*self.first_name_input_xpath)
        last_name_input.send_keys(last_name)


    def check_email(self, email):
        email_field = self.driver.find_element(*self.email_login_input_xpath)
        assert email_field.get_attribute("value") == email

    def fill_password(self, password):
        passw_input = self.driver.find_element(*self.password_input_xpath)
        passw_input.send_keys(password)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.submit_button_xpath)
        submit_button.click()
