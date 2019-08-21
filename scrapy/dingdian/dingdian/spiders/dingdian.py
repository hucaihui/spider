import scrapy
from scrapy.http import Request
from lxml import html
from dingdian.items import DingdianItem

class MySpider(scrapy.Spider):
    name = 'dingdian'

    # https://www.23us.so/list/1_1.html
    # https://www.23us.so/list/2_1.html
    allowed_domains = ['23us.so']
    base_url_front = 'https://www.23us.so/list/'
    base_url_last = '.html'
    base_url = 'https://www.23us.so/list/{}_1.html'

    # start_urls = ['https://www.23us.so/list/1_1.html']

    def start_requests(self):
        for i in range(1, 2):
            #url = self.base_url_front + str(i) + '_1' + self.base_url_last
            url = self.base_url.format(i)
            print('is running:', url)
            yield Request(url, self.parse)

    def parse(self, response):
        print('*'*150)
        max_num = response.xpath("//dd[@class='pages']//a[@class='last']/text()").extract()
        print(int(max_num[0]))
        # print(response.text)
        print(response.url[:-6])
        url_sec = str(response.url[:-6])
        for i in range(1, int(max_num[0])):
            url1 = url_sec + str(i) + self.base_url_last
            #print(url1)
            yield Request(url1, callback=self.get_name)




    def get_name(self, response):
        url_node = response.xpath("//tr[@bgcolor='#FFFFFF']")
        for node in url_node:
            item = DingdianItem()
            item['novel_name'] = node.xpath(".//a/@title").extract()[0]
            item['novel_url'] = node.xpath(".//a/@href").extract()[1]
            print(item)
            #print(novel_url)
            yield item



