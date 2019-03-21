# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SwItem(scrapy.Item):

    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    types = scrapy.Field()
    # tags = scrapy.Field()
    key = scrapy.Field()
    content = scrapy.Field()
    href = scrapy.Field()
    pass
