from __future__ import absolute_import
import scrapy
from scrapy.shell import inspect_response
#from cook import find_cookies
from onlyfinder.spiders.cook import find_cookies


class Only2Spider(scrapy.Spider):
    name = 'only2'
    url = "https://onlyfinder.com/cdn-cgi/challenge-platform/h/g/cv/result/773af6180ed99e77"
    start_urls = [url]
    
    custom_settings = {
        'COOKIES_ENABLED': True,
        'COOKIES_DEBUG': True

    }

    cookie = find_cookies()

    headers = {
        'authority': 'onlyfinder.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://onlyfinder.com',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Cookie': cookie
            }


    def start_requests(self):
        start_url = "https://onlyfinder.com/cdn-cgi/challenge-platform/h/g/cv/result/773af6180ed99e77"
        yield scrapy.Request(url=start_url, callback=self.parse, headers=self.headers)


    def parse(self, response):
        inspect_response(response.headers())
