import scrapy
import csv

from ..items import VnexpressContentItem


class QuoteSpider(scrapy.Spider):
    name = 'vnexpresscontent'
    start_urls = []

    with open('./links.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            start_urls.append(row[0])
    csvFile.close()

    def parse(self, response):
        items = VnexpressContentItem()
        sidebar = response.css('.sidebar_1')

        title = sidebar.css('.title_news_detail::text').extract()
        des = sidebar.css('p.description::text').extract()
        content = sidebar.css('p.Normal::text').extract()
        tag = response.css('ul.breadcrumb')[0].css('a::text')[0].extract()

        items['title'] = title
        items['des'] = des
        items['content'] = content
        items['tag'] = tag
        yield items
