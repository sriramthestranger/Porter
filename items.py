# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Recursive1Item(Item):
	tipText = Field()
	userName = Field()
	tipDate = Field()
