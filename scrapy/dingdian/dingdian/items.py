# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    novel_name = scrapy.Field()
    novel_url = scrapy.Field()
    author = scrapy.Field()
    novel_count = scrapy.Field()
    pass
