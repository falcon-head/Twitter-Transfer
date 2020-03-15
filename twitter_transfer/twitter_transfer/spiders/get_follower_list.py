"""
__foldername__ = twitter-transfer
__filename__ = get_follower_list.py
__author__ = Shrikrishna Joisa
__date_created__ = 14/03/2020
__date_last_modified__ =  14/03/2020
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

class FollowerList(scrapy.Spider):

    name = "get_follower_list"
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

        # Go to profile
        profile = twitter_driver.find_element_by_xpath('//nav[@aria-label="Primary"]//a[@aria-label="Profile"]')
        twitter_driver.execute_script("arguments[0].scrollIntoView()", profile)
        profile.click()
        time.sleep(10)

        # Find the following button
        following_list = twitter_driver.find_element_by_xpath('//div//a[contains(@href, "following")]')
        # twitter_driver.execute_script("arguments[0].scrollIntoView();", following_list)
        following_list.click()
        time.sleep(5)

        # Scroll and get the data
        last_scroll_height = twitter_driver.execute_script("return document.body.scrollHeight")

        while True:
            # Get the total number of followers
            length_of_follower = twitter_driver.find_elements_by_xpath('//div//section//div[contains(@aria-label, "Timeline: Following")]//div[contains(@data-testid, "UserCell")]//a//span/span')

            # Get all the username and passoword
            try:
                for i in range(0, len(length_of_follower)):
                    item = []
                    item = TwitterTransferItem()
                    name = twitter_driver.find_elements_by_xpath('//div//section//div[contains(@aria-label, "Timeline: Following")]//div[contains(@data-testid, "UserCell")]//a//span/span')[i]
                    print('*********************************************', name.text)
                    name = name.text
                    item["Name"] = name
                    yield item
            except Exception as e:
                print(e)

            twitter_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

            new_scroll_height = twitter_driver.execute_script("return document.body.scrollHeight")

            if new_scroll_height == last_scroll_height:
                break

            last_scroll_height = new_scroll_height

        print("Exited the scrolling")



    def spider_closed(self, spider):
        pass
