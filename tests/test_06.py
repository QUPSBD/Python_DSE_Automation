import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_value import CHANGE


class Test(BaseTestClass):

    def test_tc_06(self):
        index = Index(self.chrome_webdriver)
        index.click_more_button().click()
        time.sleep(5)

        latest_share_price_page_change_row = []
        for i in range(1, 382):
            change_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[8]').text
            delete_comma = change_row_value.replace(',', '')
            latest_share_price_page_change_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_change_row[i]) == str(CHANGE.change_values[i]):
                print(f"{latest_share_price_page_change_row[i]} {CHANGE.change_values[i]} pass")
            else:
                print(f"{latest_share_price_page_change_row[i]} {CHANGE.change_values[i]} failed")