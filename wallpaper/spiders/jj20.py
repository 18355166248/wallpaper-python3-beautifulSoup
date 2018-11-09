# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
import re
from wallpaper.items import WallpaperItem

num = 0

class Jj20Spider(scrapy.Spider):
    name = 'jj20'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/dongman/2.html']

    def parse(self, response):
        Soup = BeautifulSoup(response.text, "lxml")
        if 'dongman' in response.url:
            for ul in Soup.find_all('ul' ,class_='pic-list2'):
                for li in ul.find_all('li'):
                    url = li.a['href']
                    yield Request('http://desk.zol.com.cn%s'%url)
        else:
            # 判断是解析下一个页面 还是 拿图片
            lenNum = len(response.xpath('//*[@id="showImg"]/li[1]/@class').extract()[0].strip().split(' '))
            if lenNum == 2:
                for li in response.xpath('//*[@id="showImg"]/li'):
                    url1 = li.xpath('./a/@href').extract()[0]
                    yield Request('http://desk.zol.com.cn/%s' %url1)
            else:
                url2 = ''
                # 获取图片地址
                imgUrl1 = response.xpath('//*[@id="2560x1600"]/@href')
                imgUrl2 = response.xpath('//*[@id="1920x1200"]/@href')
                imgUrl3 = response.xpath('//*[@id="1920x1080"]/@href')

                if imgUrl1:
                    url2 = imgUrl1.extract()[0]
                elif imgUrl2:
                    url2 = imgUrl2.extract()[0]
                elif imgUrl3:
                    url2 = imgUrl3.extract()[0]
                yield Request('http://desk.zol.com.cn%s'%url2, dont_filter=True, callback=self.getImgUrl)


    def getImgUrl(self, response):
        print(response.xpath('//img/@src').extract()[0])
        global num
        num += 1
        urlImg = response.xpath('//img/@src').extract()[0]
        if urlImg:
            item = WallpaperItem()
            item['name'] = num
            item['url'] = urlImg
            yield item