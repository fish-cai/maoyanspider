# -*- coding: utf-8 -*-
import time
import scrapy
from scrapy.http import Request
from maoyan.items import MaoyanItem


class Maoyantop100Spider(scrapy.Spider):

    name = 'maoyanTop100'

    def start_requests(self):
        for offset in range(0, 100, 10):
            self.url = 'http://maoyan.com/board/4?offset={}'.format(offset)
            yield Request(self.url, callback=self.parse)


    def parse(self, response):
        context = response.css('dd')
        for info in context:
            item = MaoyanItem()
            item['movie'] = info.css('p.name a::text').extract_first().strip()
            item['actor'] = info.css('.star::text').extract_first().strip()
            item['release'] = info.css('.releasetime::text').extract_first().strip()
            score = info.css('i.integer::text').extract_first().strip()
            score += info.css('i.fraction::text').extract_first().strip()
            item['score'] = score
            print(item)
            yield item


































