from utails.locators import *


class Index(object):
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver
        self.locator = PageLocator

    def click_more_button(self):
        return self.chrome_webdriver.find_element(*self.locator.more_button)

    def click_volume(self):
        return self.chrome_webdriver.find_element(*self.locator.volume_button)

    def click_volume_more_button(self):
        return self.chrome_webdriver.find_element(*self.locator.volume_more_button)