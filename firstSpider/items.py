# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    house_type = scrapy.Field()
    size = scrapy.Field()
    rent_style = scrapy.Field()
    area = scrapy.Field()
    feature = scrapy.Field()
    price = scrapy.Field()





