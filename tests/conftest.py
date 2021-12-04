import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def main(request):
    chrome_webdriver = webdriver.Chrome(executable_path=r"/home/abdullah/Desktop/dhaka_stok/chromedriver_win32/chromedriver")
    chrome_webdriver.get("https://www.dsebd.org/")
    chrome_webdriver.maximize_window()
    chrome_webdriver.implicitly_wait(180)

    request.cls.chrome_webdriver = chrome_webdriver
    yield
    chrome_webdriver.close()
