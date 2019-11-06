#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/10/29 14:41
# @Author : Srunkyo
# @File   : nike.py

import scrapy
from savary.target_urls import nike_urls
from savary.items import ShoeItem

class NikeSpider(scrapy.Spider):
    name = "nike"

    def start_requests(self):
        urls = nike_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # For testing
        filename = response.url.split("/")[-1] + ".html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        titles = response.xpath('//div[@class="product-card__title"]/text()').getall()
        subtitles = response.xpath('//div[@class="product-card__subtitle"]/text()').getall()
        prices = response.xpath('//div[@class="product-card__price"]/div/div[@data-test="product-price"]/text()').getall()
        links = response.xpath('//a[@class="product-card__link-overlay"]/@href').getall()
        image_urls = response.xpath('//div[contains(@class, "product-card__hero-image")]/picture/img/@src').getall()
        map = zip(titles, subtitles, prices, links, image_urls)

        nike_items = []
        for i in map:
            nike_item = ShoeItem()
            nike_item['title'] = i[0]
            nike_item['sub_title'] = i[1]
            nike_item['price'] = float(i[2][1:])
            nike_item['link'] = i[3]
            nike_item['image_url'] = i[4]
            nike_item['source'] = "nike"
            nike_items.append(nike_item)

        return nike_items


