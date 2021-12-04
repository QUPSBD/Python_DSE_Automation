from data.market_high_xl_volume import HIGH


class HighPage(object):
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver

    def high(self):
        latest_share_price_page_high_page_row = []
        for i in range(1, 382):
            high_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[4]').text
            delete_comma = high_row_value.replace(',', '')
            latest_share_price_page_high_page_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_high_page_row[i]) == str(HIGH.high_values[i]):
                # print(f"{latest_share_price_page_high_page_row[i]}...{HIGH.high_values[i]}..... pass")
                print("pass")
            else:
                print(f"{latest_share_price_page_high_page_row[i]}--{HIGH.high_values[i]}..... failed")