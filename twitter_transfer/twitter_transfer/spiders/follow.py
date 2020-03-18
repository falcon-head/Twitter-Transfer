"""
__foldername__ = twitter-transfer
__filename__ = get_follower_list.py
__author__ = Shrikrishna Joisa
__date_created__ = 16/03/2020
__date_last_modified__ =  17/03/2020
__python_version__ = 3.7.4 64-bit
__credits__ = []

"""

import scrapy
import time
import pandas as pd
import datetime
from selenium import webdriver
from w3lib.html import remove_tags
from scrapy import signals
from pydispatch import dispatcher
from scrapy.http import FormRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.webdriver.common.keys import Keys
from w3lib.html import remove_tags
from twitter_transfer.items import TwitterTransferItem
from twitter_transfer import settings
from tqdm import tqdm


class Follow(scrapy.Spider):

    name = "follow"
    allowed_domains = ['twitter.com']
    email = ''
    password = ''

    def __init__(self, email = '', password= '', **kwargs):
        """Notify when the spider is closed

        Keyword Arguments:
            name {[type]} -- [description] (default: {None})
        """

        #* Assign the values
        self.email = email
        self.password = password

        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def start_requests(self):
        yield scrapy.Request('https://twitter.com/', callback=self.parse)

    def parse(self, response):

        #* Initialize the drivers
        # Chrome options
        chrome_option = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_option.add_experimental_option("prefs",prefs)
        chrome_option.add_argument("--disable-gpu-sandbox")
        chrome_option.add_argument("--incognito")
        chrome_option.add_argument("--disable-infobars")
        chrome_option.add_argument("--start-maximized")
        twitter_driver = webdriver.Chrome(chrome_options=chrome_option)
        twitter_driver.set_script_timeout(4000000)
        twitter_driver.set_page_load_timeout(180000)

        # Get the url
        twitter_driver.get(response.url)
        time.sleep(5)

        #Find the login button and click
        login_button = twitter_driver.find_element_by_xpath('//div//a[contains(@data-testid, "login")]')
        twitter_driver.execute_script("arguments[0].scrollIntoView();", login_button)
        login_button.click()
        time.sleep(5)

        #Find the username input
        username_input = twitter_driver.find_element_by_xpath('//div//label//input[contains(@name, "session[username_or_email]")]')
        twitter_driver.execute_script("arguments[0].scrollIntoView();", username_input)
        username_input.send_keys(self.email)
        time.sleep(5)

        # Find the password field
        password_input = twitter_driver.find_element_by_xpath('//div//label//input[@type="password"]')
        twitter_driver.execute_script("arguments[0].scrollIntoView();", password_input)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(15)

        # Go to Search field and search for the all the item in csv or pdf

        # TODO: Produce Output in CSV
        # TODO: Convert to df
        # TODO: Pass the each username column to the twitter search bar
        # TODO: Find the click on the each username and follow the follow button and repeat

        df = pd.read_csv('test.csv')
        df = df.drop_duplicates()
        follower_list = df['Username'].tolist()

        for i in tqdm(follower_list, desc='Following'):

            search_people = twitter_driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
            twitter_driver.execute_script('arguments[0].scrollIntoView();', search_people)
            search_people.send_keys(i)
            time.sleep(4)

            try:

                # Xpath to click //div[@role="listbox"]//div[@data-testid="TypeaheadUser"]//div[@role="presentation"]
                drop_down_list = twitter_driver.find_elements_by_xpath('//div[@role="listbox"]//div[@data-testid="TypeaheadUser"]//div[@role="presentation"]')[1]
                twitter_driver.execute_script('arguments[0].scrollIntoView();', drop_down_list)
                drop_down_list.click()
                time.sleep(5)

            except:

                # Xpath to click //div[@role="listbox"]//div[@data-testid="TypeaheadUser"]//div[@role="presentation"]
                drop_down_list = twitter_driver.find_element_by_xpath('//div[@role="listbox"]//div[@data-testid="TypeaheadUser"]//div[@role="presentation"]')
                twitter_driver.execute_script('arguments[0].scrollIntoView();', drop_down_list)
                drop_down_list.click()
                time.sleep(5)


    def spider_closed(self, spider):
        pass

