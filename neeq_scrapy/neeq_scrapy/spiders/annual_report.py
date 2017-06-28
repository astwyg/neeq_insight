# -*- coding: utf-8 -*-
import scrapy
import time, re

def get_content(raw_str):
    finder = re.findall("(?<=[(])[^()]+\.[^()]+(?=[)])",raw_str)
    assert len(finder) == 1
    return finder[0]

class AnnualReportSpider(scrapy.Spider):
    name = 'annual_report'
    allowed_domains = ['*']
    start_urls = ['http://www.neeq.com.cn/nqxxController/nqxx.do?callback=jQuery18305900115946886557_1498659199537&page=0&typejb=T&xxzqdm=&xxzrlx=&xxhyzl=&xxssdq=&sortfield=xxzqdm&sorttype=asc&dicXxzbqs=&xxfcbj=&_={}']

    def start_requests(self):
        self.ts = int(time.time()*1000)
        start_url = self.start_urls[0]
        yield scrapy.Request(start_url.format(self.ts), callback=self.get_conpany_lists)

    def get_conpany_lists(self, response):
        max_page = response.xpath("//div[@class='page']/a[-2]/text").extract()
