# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ForumUser(scrapy.Item):
    """
    example)
    https://forums.oneplus.net/members/karan-kadakia.481070/
    """
    user_id = scrapy.Field()

class ForumThread(scrapy.Item):
    """
    example)
    https://forums.oneplus.net/threads/faq-frequently-asked-questions-including-carrier-compatibility.7195/
    https://forums.oneplus.net/threads/faq-frequently-asked-questions-including-carrier-compatibility.7195/page-2
    """

    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()

class ThreadComment(scrapy.Item):
    user = scrapy.Field()
    date = scrapy.Field()
    parent_thread = scrapy.Field()



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