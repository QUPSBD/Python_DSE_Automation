import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_value import TRADE


class Test(BaseTestClass):

    def test_tc_07(self):
        index = Index(self.chrome_webdriver)
        index.click_more_button().click()
        time.sleep(5)

        latest_share_price_page_trade_row = []
        for i in range(1, 382):
            trade_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[9]').text
            delete_comma = trade_row_value.replace(',', '')
            latest_share_price_page_trade_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_trade_row[i]) == str(TRADE.trade_values[i]):
                print(f"{latest_share_price_page_trade_row[i]} {TRADE.trade_values[i]} pass")
            else:
                print(f"{latest_share_price_page_trade_row[i]} {TRADE.trade_values[i]} failed")