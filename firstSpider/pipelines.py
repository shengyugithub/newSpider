# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.exporters import JsonLinesItemExporter
#
# class FirstspiderPipeline(object):
#
#     def __init__(self):
#         self.file = open('456.json','wb')
#         self.exporter = JsonLinesItemExporter(self.file, encoding="utf-8",ensure_ascii=False)
#         self.exporter.start_exporting()
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.file.close()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

import re
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi

class HousePipeline(object):
    @classmethod
    def from_settings(cls, settings):
    # 获取settings文件中的配置
        dbparams = dict(host=settings['MYSQL_HOST'],
                        db=settings['MYSQL_DBNAME'],
                        user=settings['MYSQL_USER'],
                        passwd=settings['MYSQL_PASSWORD'],
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor,
                        use_unicode=True
                        )

        dbpool=adbapi.ConnectionPool('pymysql', **dbparams)

        return cls(dbpool)

    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        # 使用数据库连接池对象进行数据库操作,自动传递cursor对象到第一个参数
        query=self.dbpool.runInteraction(self.do_insert, item)
        # 设置出错时的回调方法,自动传递出错消息对象failure到第一个参数
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        spider.logger.error(failure)

    def do_insert(self, cursor, item):
        #修改 繁琐
        location_district = ''
        location_street = ''
        location_community = ''
        if len(item['area'])==3:
            location_district = item['area'][0]
            location_street = item['area'][1]
            location_community = item['area'][2]
        elif len(item['area'])==2:
            location_district = item['area'][0]
            location_street = item['area'][1]
            location_community = ''
        price = int(item['price'])
        #size = int(item['size'])
        #print(item['size'])
        #print(type(item['size']))
        size = int(re.findall(r'[0-9]*', item['size'])[0])


        insert_sql = "INSERT INTO newhouse_detail(house_title, house_type, house_size,rent_style, rent_price,location_district,location_street,location_community,feature)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_sql,(item['title'], item['house_type'], size, item['rent_style'], price, location_district, location_street, location_community,item['feature']))


        # insert_sql = "INSERT INTO house_detail(house_title, house_type, house_size,rent_style, rent_price)VALUES (%s,%s,%s,%s,%s)"
        # cursor.execute(insert_sql,(item['title'], item['house_type'], item['size'], item['rent_style'], item['price'] ))