import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_volume import LTP
from pages.ltp_row import LTPPage


class Test(BaseTestClass):

    def test_tc_10(self):
        index = Index(self.chrome_webdriver)
        index.click_volume().click()
        index.click_volume_more_button().click()
        time.sleep(5)
        ltp_row = LTPPage(self.chrome_webdriver)
        ltp_row.ltp()
