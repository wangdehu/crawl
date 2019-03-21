# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# import sw.settings

class SwPipeline(object):
    def __init__(self):
        self.con = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='stu', charset='utf8')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):

        sql =" insert into topics (title,date,types,keyes,content,author,href) select '%s' ,'%s','%s','%s','%s','%s','%s' " % ( item["title"],item["date"],item["types"],item["key"],item["content"],item["author"],item["href"])
        sql = sql +"from dual where  not exists ( select * from "
        sql = sql +"topics where types='%s' and keyes='%s'); " %(item["types"],item["key"])



        # print("*********************************************")
        
        # print(sql)

        # print("*********************************************")

        self.cur.execute(sql)
        self.con.commit()
        return item

    def spider_closed(self, spider):
        self.cur.close()
        self.con.close()
