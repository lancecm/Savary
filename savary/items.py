# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SavaryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ShoeItem(scrapy.Item):
    title = scrapy.Field()
    sub_title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    image_url = scrapy.Field()
    source = scrapy.Field()


