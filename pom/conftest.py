import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


EXECUTABLE_PATH = '/usr/local/bin/chromedriver'


@pytest.fixture(scope='session')
def web_driver():
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=chrome-data")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.quit()
