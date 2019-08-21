# -*- coding: utf-8 -*-
import scrapy
from quotetutorial.items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrapy.com']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self, response):
        #print(response.text)
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuotetutorialItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()  #extract_first第一个
            tags = quote.css('.tags .tag::text').extract()        #extract全部
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item      #此处为生成器

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)   #生成url
        print('is runing:', url)
        #refer: https://blog.csdn.net/lvqiuyao/article/details/76841663
        if url is not None:
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)

