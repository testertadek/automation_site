from selenium.webdriver.common.by import By

class Header:

    slider = (By.XPATH, '//*[@id="homepage-slider"]//div[@class = "bx-viewport"]')
    right_top_banner = (by.XPATH, '//*[@id="htmlcontent_top|"]//li[1]/a')
    right_bottoom_banner = (by.XPATH, '//*[@id="htmlcontent_top|"]//li[2]/a')

    # to do make more locators
