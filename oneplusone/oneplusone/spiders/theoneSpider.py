# -*- coding: utf-8 -*-

__author__ = 'ungsik'
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from oneplusone.items import ThreadComment

class TheoneSpider(CrawlSpider):

    name = "theOne"

    allowed_domains = ["forums.oneplus.net"]

    start_urls = [
        "https://forums.oneplus.net/forums/announcements/",
        "https://forums.oneplus.net/forums/contests/",
        "https://forums.oneplus.net/forums/the-one/",
        "https://forums.oneplus.net/forums/cyanogenmod-11s/",
        "https://forums.oneplus.net/forums/dev-roms/",
        "https://forums.oneplus.net/forums/accessories/",
        "https://forums.oneplus.net/forums/invites/",
        "https://forums.oneplus.net/forums/off-topic/",
        "https://forums.oneplus.net/forums/introduce-yourself/",
        "https://forums.oneplus.net/forums/tech-talk/",
        "https://forums.oneplus.net/forums/fan-gatherings/",
    ]

    rules = (
        Rule(LinkExtractor(allow=('threads\/.+', )), callback='parse_thread', follow=True),
    )


    def parse_thread(self, response):

        items = []

        forum_name = response.xpath('//*[@id="top"]/div/div/div[1]/nav/fieldset/span/span[3]/a/span/text()').extract()
        thread_title = response.xpath('//*[@id="top"]/div/div/div[2]/h1/text()').extract()
        thread_url = response.url

        comment_list = response.xpath('//li[@class="message   "]')

        for comment in comment_list:
            item = ThreadComment()
            item['user_url'] = comment.xpath('.//h3/a[@class="username"]/@href').extract()
            item['date'] = comment.xpath('.//*[@class="DateTime"]/text()').extract()

            item['forum_name'] = forum_name
            item['thread_title'] = thread_title
            item['thread_url'] = thread_url

            items.append(item)
            # print item
        return items

