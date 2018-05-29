# -*- coding: utf-8 -*-
import scrapy


class StartSpider(scrapy.Spider):
    name = 'start'
    allowed_domains = ['www.csindex.com.cn']

    # 上证50 ：http://www.csindex.com.cn/zh-CN/indices/index-detail/000016
    # 沪深300：http://www.csindex.com.cn/zh-CN/indices/index-detail/000300
    # 中证500：http://www.csindex.com.cn/zh-CN/indices/index-detail/000905
    start_urls = [
        'http://www.csindex.com.cn/zh-CN/indices/index-detail/000016',
        'http://www.csindex.com.cn/zh-CN/indices/index-detail/000300',
        'http://www.csindex.com.cn/zh-CN/indices/index-detail/000905',
    ]

    def parse(self, response):
        pass
