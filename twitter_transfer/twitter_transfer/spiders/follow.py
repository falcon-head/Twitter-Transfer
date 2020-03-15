"""
__foldername__ = twitter-transfer
__filename__ = get_follower_list.py
__author__ = Shrikrishna Joisa
__date_created__ = 16/03/2020
__date_last_modified__ =  16/03/2020
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


class Follow(scrapy.Spider):

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

    def spider_closed(self, spider):
        pass