# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class WallpaperPipeline(object):
    def process_item(self, item, spider):
        # def Schedule(a, b, c):
        #     per = 100.0 * a * b / c
        #     if per > 100:
        #         per = 100
        #         print('完成！')
        #     print('%.2f%%' % per)
        file_name = os.path.join('/Users/seven/Pictures', str(item['name']) + '.jpg')
        urllib.request.urlretrieve(item['url'], file_name)
