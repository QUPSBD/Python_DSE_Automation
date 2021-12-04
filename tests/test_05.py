import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_value import YCP


class Test(BaseTestClass):

    def test_tc_05(self):
        index = Index(self.chrome_webdriver)
        index.click_more_button().click()
        time.sleep(5)

        latest_share_price_page_ycp_row = []
        for i in range(1, 382):
            ycp_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[7]').text
            delete_comma = ycp_row_value.replace(',', '')
            latest_share_price_page_ycp_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_ycp_row[i]) == str(YCP.ycp_values[i]):
                print(f"{latest_share_price_page_ycp_row[i]} {YCP.ycp_values[i]} pass")
            else:
                print(f"{latest_share_price_page_ycp_row[i]} {YCP.ycp_values[i]} failed")