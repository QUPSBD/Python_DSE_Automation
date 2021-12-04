import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from pages.high_row import HighPage


class Test(BaseTestClass):

    def test_tc_11(self):
        index = Index(self.chrome_webdriver)
        index.click_volume().click()
        index.click_volume_more_button().click()
        time.sleep(5)

        high_row = HighPage(self.chrome_webdriver)
        high_row.high()
