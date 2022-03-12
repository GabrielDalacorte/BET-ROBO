import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

from xpaths import page_data


class InitBrowser(object):

    def __init__(self, url):
        self.url = url
        self.driver = None

    def init(self):
        option = Options()
        option.headless = True
        self.driver = webdriver.Chrome(options=option)  # not open google

        self.driver.get(self.url)
        self.driver.quit()

        #time.sleep(10)

        return self.driver

    def extract_data(self, init):

        self.driver.find_element_by_xpath(page_data)

        html_content = self.driver.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')


if __name__ == "__main__":

    init_data = InitBrowser(url='https://www.bet365.com/#/AS/B4/') #Galgo Example

    init_data.extract_data(init_data.init())

