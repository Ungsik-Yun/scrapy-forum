# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OneplusoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ForumUser(scrapy.Item):
	'''
	example)
	https://forums.oneplus.net/members/karan-kadakia.481070/
	'''
	pass

class ForumThread(scrapy.Item):
	'''
	example)
	https://forums.oneplus.net/threads/faq-frequently-asked-questions-including-carrier-compatibility.7195/
	https://forums.oneplus.net/threads/faq-frequently-asked-questions-including-carrier-compatibility.7195/page-2
	'''
	pass

class TheOneForum(scrapy.Item):
	pass




'''
https://forums.oneplus.net/forums/announcements/
https://forums.oneplus.net/forums/contests/

https://forums.oneplus.net/forums/the-one/
https://forums.oneplus.net/forums/cyanogenmod-11s/
https://forums.oneplus.net/forums/dev-roms/
https://forums.oneplus.net/forums/accessories/
https://forums.oneplus.net/forums/invites/

https://forums.oneplus.net/forums/off-topic/
https://forums.oneplus.net/forums/introduce-yourself/
https://forums.oneplus.net/forums/tech-talk/
https://forums.oneplus.net/forums/fan-gatherings/

'''