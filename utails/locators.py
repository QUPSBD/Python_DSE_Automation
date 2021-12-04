from selenium.webdriver.common.by import By

class PageLocator(object):
    # "//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[1]/tr/td[3]"
    # "//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[2]/tr/td[3]"

    more_button = (By.XPATH, '//*[@id="value"]/div/table/tbody/tr[7]/td/a/strong')
    volume_button = (By.XPATH, '/html/body/div[2]/section/div/div[4]/div[3]/div[2]/div/div[1]/ul/li[2]/a')
    volume_more_button = (By.XPATH, '//*[@id="volume"]/div/table/tbody/tr[7]/td/a/strong')
    # ltp_value = (By.XPATH, '//*[@id="RightBody"]/div[1]/div[2]/div[1]/div[2]/table/tbody[1]/tr/td[3]')


