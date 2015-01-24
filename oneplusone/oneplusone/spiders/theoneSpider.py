# -*- coding: utf-8 -*-

__author__ = 'ungsik'
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from oneplusone.items import ForumThread

class TheoneSpider(CrawlSpider):

    name = "theOne"

    allowed_domains = ["forums.oneplus.net"]

    start_urls = [
        # "https://forums.oneplus.net/forums/announcements/",
        # "https://forums.oneplus.net/forums/contests/",
        "https://forums.oneplus.net/forums/the-one/",
        # "https://forums.oneplus.net/forums/cyanogenmod-11s/",
        # "https://forums.oneplus.net/forums/dev-roms/",
        # "https://forums.oneplus.net/forums/accessories/",
        # "https://forums.oneplus.net/forums/invites/",
        # "https://forums.oneplus.net/forums/off-topic/",
        # "https://forums.oneplus.net/forums/introduce-yourself/",
        # "https://forums.oneplus.net/forums/tech-talk/",
        # "https://forums.oneplus.net/forums/fan-gatherings/",
    ]

    rules = (
        Rule(LinkExtractor(allow=('threads\/.+', )), callback='parse_thread', follow=True),
    )


    @classmethod
    def parse_forum(response):
        threads_list = response.xpath('//div[@class="titleText"]')
        for thread in threads_list:
            item = ForumThread()
            item['forum'] = response.xpath('//div[@class="titleBar"]/h1/text()').extract()
            item['title'] = thread.xpath('.//a[@class="PreviewTooltip"]/text()').extract()
            item['url'] = thread.xpath('.//a[@class="PreviewTooltip"]/@href').extract()

            # 날짜를 추출. 각 쓰레드는 1~2개의 날짜를 가질 수 있는데, 처음 것은 쓰여진 날, 두번째는 마지막 리플레이가 달린 날이다.
            # temp_date = thread.xpath('.//a[@class="faint"]/abbr[@class="DateTime"]/text()').extract()
            #
            # if temp_date:
            #     item['date'] = thread.xpath('.//a[@class="dateTime"]/abbr[@class="DateTime"]/text()').extract()
            # else:
            #     item['date'] = temp_date

            item['date'] = thread.xpath('.//abbr[@class="DateTime"]/text()').extract()


            print item
        return item

    def parse_thread(self, response):
        item = ForumThread()
        item['forum'] = response.xpath('//*[@id="top"]/div/div/div[1]/nav/fieldset/span/span[3]/a/span/text()').extract()
        item['title'] = response.xpath('//*[@id="top"]/div/div/div[2]/h1/text()').extract()
        item['url'] = response.url
        # item['date'] = thread.xpath('.//abbr[@class="DateTime"]/text()').extract()

        print item
        return item

