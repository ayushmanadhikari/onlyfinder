import scrapy
from urllib.parse import urljoin




class OnlySpider(scrapy.Spider):
    name = 'only'

    COOKIE = "_r=1670044731.; _l=1670044731.; __cf_bm=ALv.XhiGuf3jb59HtxByNq5bnB4ex11jVba6CntD9mM-1670044731-0-AclDMCe9MwpEoO/jFBgVi2RsQ7dWoKnAPbk6mYpYkhlkWb/DaEDAfnbfTOnMqUe6LldKIf3PfPo6PUzonqwSVA38URueWb//aG4dnIovMqd7YFFVx9U/5iava1fyZYNJf2AeO5DsB6jN/r2Cn2tFniY=; _ga=GA1.2.1787214459.1670044732; _gid=GA1.2.1412854470.1670044732; _gat_gtag_UA_181000007_1=1; _ga_1PB9XEPVWM=GS1.1.1670044732.1.1.1670044790.2.0.0"

    base_url = "https://onlyfinder.com/"

    my_headers = {
        'authority': 'onlyfinder.com',
        'method': 'GET',
        'path': '/json/search?q=oklahoma%20onlyfans&start=0&first=true',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        #'cookie': '_r=1670044731.; _l=1670044731.; _gid=GA1.2.1412854470.1670044732; __cf_bm=X5vKn.cbgs1ND2hAi58luo9IphuR5eoea5hr5qUAT.c-1670049139-0-AQv14lHX6fe/ouy5HTRPQokVbV+V8fEXWYkfvbeubC+00poV3EjhUzv8Ji+GA50oR+BsLiiwRp6D961nzluFg4uCVjNVaALRJV/U2NEed0/tood/p1U92oRWM8i/PdLkhJTAH1GCaCxaeJjIID3vTaE=; _ga=GA1.2.1787214459.1670044732; _ga_1PB9XEPVWM=GS1.1.1670049139.2.1.1670049220.60.0.0',
        #'cookie': '_r=1670044731.; _l=1670044731.; _gid=GA1.2.1412854470.1670044732; __cf_bm=59Zh733IC0711Noq8hxquL4xG1U6IDJowzmLu1U6OaU-1670056970-0-AbbtpOGrwwyz3aiVPSZRRh%2FYQI0n8v8Qhljh9a2CbzmCfY8gk1dU1b0r%2BjBEPg6GyOk7yEQZX1qMY2E3cEGTaNg%3D _ga=GA1.2.1787214459.1670044732; _ga_1PB9XEPVWM=GS1.1.1670049139.2.1.1670049220.60.0.0'
        'pragma': 'no-cache',
        'referer': 'https://google.com', 
        #'https://onlyfinder.com/oklahoma-onlyfans/profiles/',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-bc': '13a235fe',
        'x-requested-with': 'XMLHttpRequest'
    }
    

    def start_requests(self):
        start_url = "https://onlyfinder.com/"
        yield scrapy.Request(url=start_url, callback=self.parse, meta={'playwright': True}, headers=self.my_headers)



    def parse(self, response):
        types = response.xpath("//ul[@class='cloud']/li")
        type = types.xpath("//a/@href").get()
        yield scrapy.Request(url=type, callback=self.parse_cat_profile_list, meta={'playwright': True}, headers=self.my_headers)
        # for type in types:
        #     cat = type.xpath(".//a/@href").get()
        #     full_url = urljoin(self.base_url, cat)
        #     yield {
        #         'url': full_url
        #     }
            #scrapy.Request(url=full_url, callback=self.parse_cat_profile_list, meta={'playwright': True}, headers=self.my_headers)
    

    def parse_cat_profile_list(self, response):
        results = response.xpath("//div[@class='result']")
        for result in results:
            name = result.xpath("//div//h3").get()
            yield {
                'name': name
            }


        #//div[@class='result']//div//h3