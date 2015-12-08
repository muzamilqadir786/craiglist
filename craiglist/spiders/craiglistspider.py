# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from craiglist.items import CraiglistItem
import time

class CraiglistspiderSpider(scrapy.Spider):
    name = "craiglistspider"
    allowed_domains = ["craiglist.org"]
    start_urls = (
        'http://www.google.com/',
    )

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get('http://craiglist.org')


