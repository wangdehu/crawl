# -*- coding: utf-8 -*-
import scrapy
import re
from bm.items import BmStuItem

class BmTeaSpider(scrapy.Spider):
    name = 'bm_tea'
    url = 'http://bm.cugb.edu.cn/jwc/jszq/'
    allowed_domains = ['bm.cugb.edu.cn']
    start_urls = ['http://bm.cugb.edu.cn/jwc/jszq/']

    def parse(self, response):
        ls = response.css('ul.listUl')
        for news in ls.css('li'):
            urls = self.url + news.css('a::attr(href)').extract_first()[8:] 
            title = news.css('a::text').extract_first()
            key = news.css('a::attr(href)').extract_first()[8:14]
            # print(urls)
            yield scrapy.Request(urls,meta={'title':title ,'key':key},callback=self.parse_content)
        
    def parse_content(self,response):

        item = BmStuItem()
        item["href"] =response.url
        item["key"] = response.meta["key"]
        item["title"] =response.meta["title"]
        
        head_str_split = response.css('div.sourceDetail').css('h3').extract_first().split('\xa0')

        item["author"] = head_str_split[0][7:]
        item["date"] = head_str_split[2][5:]
        item["types"] = "bm_tea"
        content_list =response.xpath('/html[1]/body[1]/div[1]/div[3]/div[2]/div[3]//text()').extract()
        item["content"] = "".join(content_list)

        yield item



        
        