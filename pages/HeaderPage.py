from selenium.webdriver.common.by import By
from automation_site.pages.BasePage import BasePage

class HeaderPage(BasePage):

    sale_off_banner_xpath = (By.XPATH, '//*[@id="header"]//*[@class="banner"]')
    span_shop_phone_xpath = (By.XPATH, '//*[@id="header"]//*[@class="shop-phone"]')
    contact_link_xpath = (By.XPATH, '//*[@id="header"]//*[@id="contact-link"]')
    login_link_xpath = (By.XPATH, '//*[@id="header"]//a[@class="login"]')




    def click_login_link(self):
        login_link = self.driver.find_element(*self.login_link_xpath)
        login_link.click()
