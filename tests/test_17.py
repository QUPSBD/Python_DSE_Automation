import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from data.market_high_xl_volume import VALUES


class Test(BaseTestClass):

    def test_tc_17(self):
        index = Index(self.chrome_webdriver)
        index.click_volume().click()
        index.click_volume_more_button().click()
        time.sleep(5)

        latest_share_price_page_value_row = []
        for i in range(1, 382):
            values_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[10]').text
            delete_comma = values_row_value.replace(',', '')
            latest_share_price_page_value_row.append(delete_comma)

        for i in range(381):
            if float(latest_share_price_page_value_row[i]) == float(VALUES.value_row_values[i]):
                print(f"{latest_share_price_page_value_row[i]} {VALUES.value_row_values[i]} pass")
            else:
                print(f"{latest_share_price_page_value_row[i]} {VALUES.value_row_values[i]} failed")