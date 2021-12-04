import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_value import CLOSEP


class Test(BaseTestClass):

    def test_tc_13(self):
        index = Index(self.chrome_webdriver)
        index.click_more_button().click()
        time.sleep(5)

        latest_share_price_page_closep_row = []
        for i in range(1, 382):
            closep_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[6]').text
            delete_comma = closep_row_value.replace(',', '')
            latest_share_price_page_closep_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_closep_row[i]) == str(CLOSEP.closep_values[i]):
                print(f"{latest_share_price_page_closep_row[i]} {CLOSEP.closep_values[i]} pass")
            else:
                print(f"{latest_share_price_page_closep_row[i]} {CLOSEP.closep_values[i]} failed")