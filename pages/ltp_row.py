from data.market_high_xl_volume import LTP


class LTPPage(object):
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver

    def ltp(self):
        latest_share_price_page_ltp_page_row = []
        for i in range(1, 382):
            ltp_row_value = self.chrome_webdriver.find_element_by_xpath(f'//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[{i}]/tr/td[3]').text
            delete_comma = ltp_row_value.replace(',', '')
            latest_share_price_page_ltp_page_row.append(delete_comma)

        for i in range(381):
            if str(latest_share_price_page_ltp_page_row[i]) == str(LTP.ltp_values[i]):
                print(f"{latest_share_price_page_ltp_page_row[i]}...{LTP.ltp_values[i]}..... pass")
                # print("pass")
            else:
                print(f"{latest_share_price_page_ltp_page_row[i]}--{LTP.ltp_values[i]}..... failed")
