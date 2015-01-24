# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThreadComment(scrapy.Item):
    forum_name = scrapy.Field()
    thread_title = scrapy.Field()
    thread_url = scrapy.Field()
    date = scrapy.Field()
    user_url = scrapy.Field()



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