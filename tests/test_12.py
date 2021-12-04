import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from pages.low_row import LowPage


class Test(BaseTestClass):

    def test_tc_12(self):
        index = Index(self.chrome_webdriver)
        index.click_volume().click()
        index.click_volume_more_button().click()
        time.sleep(5)
        low_row = LowPage(self.chrome_webdriver)
        low_row.low()

