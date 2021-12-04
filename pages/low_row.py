from data.market_high_xl_volume import LOW


class LowPage(object):
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver

    def low(self):
        latest_share_price_page_low_row = []
        for i in range(1, 382):
            low_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[5]').text
            delete_comma = low_row_value.replace(',', '')
            latest_share_price_page_low_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_low_row[i]) == str(LOW.low_values[i]):
                print(f"{latest_share_price_page_low_row[i]} {LOW.low_values[i]} pass")
            else:
                print(f"{latest_share_price_page_low_row[i]} {LOW.low_values[i]} failed")