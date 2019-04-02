# -*- coding: utf-8 -*-
import scrapy
from BaiduSpider.items import BaiduspiderItem
from scrapy import Request, selector


# 爬取百度百科
"""
class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E7%B3%96%E5%B0%BF%E7%97%85']

    def start_requests(self):
        with open('urls.txt') as f:
            while 1:
                url = f.readline()
                if not url:
                    break
                else:
                    yield Request(url.strip(), callback=self.parse)

    def parse(self, response):
        item = BaiduspiderItem()
        content = response.xpath("//div[@label-module='para']")
        info = content.xpath('string(.)').extract()
        info.append('\n')
        for each in info:
            item['contents'] = each
            yield item
"""


# 爬取医学百科电子书
class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['www.a-hospital.com']
    start_urls = ['http://www.a-hospital.com/w/%E5%88%86%E7%B1%BB:%E5%9B%BE%E4%B9%A6%E7%9B%AE%E5%BD%95']
    base_url = 'http://www.a-hospital.com'

    def parse(self, response):
        urls = response.xpath("//*[@id='mw-pages']//a/@href").extract()
        book_names = response.xpath("//*[@id='mw-pages']//a/text()").extract()
        assert len(urls) == len(book_names)
        urls_to_crawl = []
        for i in range(len(book_names)):
            if book_names[i][-2:] == '目录':
                urls_to_crawl.append(urls[i])

        for url in urls_to_crawl:
            yield Request(self.base_url + url, callback=self.parse_book)

    def parse_book(self, response):
        urls = response.xpath("//*[@id='bodyContent']/div[4]//a/@href").extract()
        for url in urls:
            yield Request(self.base_url + url, callback=self.parse_content)

    def parse_content(self, response):
        item = BaiduspiderItem()

        content = response.xpath("//*[@id='bodyContent']/p")
        content = content.xpath('string(.)').extract()

        content2 = response.xpath("//*[@id='bodyContent']/ul")
        content2 = content2.xpath('string(.)').extract()
        for each in content+content2:
            item['contents'] = "".join(each.split('\xa0'))
            yield item



