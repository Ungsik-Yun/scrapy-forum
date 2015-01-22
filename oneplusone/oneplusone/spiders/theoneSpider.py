__author__ = 'ungsik'
from scrapy import Spider
from oneplusone.items import ForumThread

class TheoneSpider(Spider):

    name = "theOne"

    allowed_domains = ["https://forums.oneplus.net/"]

    start_urls = [
        "https://forums.oneplus.net/forums/the-one/"
    ]

    def parse(self, response):

        threads_list = response.xpath('//div[@class="titleText"]')
        for thread in threads_list:
            item = ForumThread()
            item['title'] =  thread.xpath('.//a[@class="PreviewTooltip"]/text()').extract()
            item['url'] = thread.xpath('.//a[@class="PreviewTooltip"]/@href').extract()

            # 날짜를 추출. 각 쓰레드는 1~2개의 날짜를 가질 수 있는데, 처음 것은 쓰여진 날, 두번째는 마지막 리플레이가 달린 날이다.
            temp_date = thread.xpath('.//a[@class="faint"]/abbr[@class="DateTime"]/text()').extract()

            if temp_date:
                item['date'] = thread.xpath('.//a[@class="dateTime"]/abbr[@class="DateTime"]/text()').extract()
            else:
                item['date'] = temp_date


            print item
