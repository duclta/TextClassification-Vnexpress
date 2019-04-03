# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VnexpressLinkItem(scrapy.Item):
    link = scrapy.Field()

class VnexpressContentItem(scrapy.Item):
    title = scrapy.Field()
    des = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
