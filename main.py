import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
from xpaths import page_data


class InitBrowser(object):

    def __init__(self, url):
        self.url = url
        self.driver = any
        self.values = any

    def init(self):
        option = Options()
        option.headless = False

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)  # not open google

        self.driver.get(self.url)
        time.sleep(15)

        return self.driver

    def extract_data(self, init):

        self.values = init.find_element(By.XPATH, page_data)

        html_content = self.values.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')

        print(type(soup))
        for x in soup:
            print(x)
        #self.driver.quit()


if __name__ == "__main__":

    init_data = InitBrowser(url='https://www.bet365.com/#/AS/B4/') #Galgo Example
    init_data.extract_data(init_data.init())

