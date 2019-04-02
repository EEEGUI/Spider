# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduspiderPipeline(object):
    def __init__(self):
        # 打开(创建)文件
        self.file = open('outputs/medicalbaike3.txt', mode='a')

    def process_item(self, item, spider):
        self.file.write(item['contents'])
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
