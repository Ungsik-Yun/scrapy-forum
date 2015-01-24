# -*- coding: utf-8 -*-

__author__ = 'ungsik'
from scrapy import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from oneplusone.items import ThreadComment


class TheoneSpider(CrawlSpider):

    name = "theOne"

    # crawl spider only crawl on "allowed_domains"
    allowed_domains = ["forums.oneplus.net"]

    # starting url for spider
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

    """
    if spider find a link on "start_urls" and examine that link pass the "rules".
    if the link pass the "rules", then add that link to 'crawl list'(may be)
    after spider crawl the link in 'crawl list', then call "callback" function in "Rule".
    spider would crawl entire site until there are no link pass the "rules" on "allowed_domains"
    """
    rules = (
        Rule(LinkExtractor(allow=('threads\/.+', )), callback='parse_thread', follow=True),
    )

    """
    this is callback function for "Rule"
    if you want dynamic parsing by url pattern,
    write more parse function and assign callback function to Rule
    """
    def parse_thread(self, response):

        # for returning result
        items = []

        # these variables are can get from response page like "threads/<thread-title>(/<page-number>)"
        forum_name = response.xpath('//*[@id="top"]/div/div/div[1]/nav/fieldset/span/span[3]/a/span/text()').extract()
        thread_title = response.xpath('//*[@id="top"]/div/div/div[2]/h1/text()').extract()
        thread_url = response.url

        # Get comment list on response page
        # onepulsone forum use "message   "(3 spaces) for message(called comment in code)
        comment_list = response.xpath('//li[@class="message   "]')

        # parsing single comment
        for comment in comment_list:
            item = ThreadComment()

            # get user unique url
            item['user_url'] = comment.xpath('.//h3/a[@class="username"]/@href').extract()

            """
            get wrote date of comment.
            if comment has been edited, date value could be 2. and, order of date is like this
            [<edited date>, <wrote date>]
            so, you can use date[-1] for always choose wrote date
            """
            item['date'] = comment.xpath('.//*[@class="DateTime"]/@title').extract()[-1]

            item['forum_name'] = forum_name
            item['thread_title'] = thread_title
            item['thread_url'] = thread_url


            items.append(item)

        return items

