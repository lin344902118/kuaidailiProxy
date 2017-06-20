# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ProxyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = Field()
    port = Field()
    status = Field()
    type = Field()
    address = Field()
    speed = Field()
    last_validate_time = Field()
