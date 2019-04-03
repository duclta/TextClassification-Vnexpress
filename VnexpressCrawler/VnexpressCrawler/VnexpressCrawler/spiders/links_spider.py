import scrapy
from ..items import VnexpressLinkItem

class QuoteSpider(scrapy.Spider):
    name = 'vnexpresslink'
    start_urls = []

    urls = [
        'https://vnexpress.net/thoi-su-p',
        'https://vnexpress.net/the-gioi-p',
        'https://vnexpress.net/kinh-doanh/p',
        'https://vnexpress.net/giai-tri/p',
        'https://vnexpress.net/the-thao/p',
        'https://vnexpress.net/phap-luat-p',
        'https://vnexpress.net/suc-khoe/p'
    ]
    for i in range(500):
        for j in range(len(urls)):
            start_urls.append(urls[j] + str(i+1))

    def parse(self, response):
        items = VnexpressLinkItem()
        sidebar = response.css('.sidebar_1')
        listnews = sidebar.css('.list_news')
        for i in listnews:
            link = i.css('a')[0].xpath('@href').extract()
            items['link'] = link
            yield items