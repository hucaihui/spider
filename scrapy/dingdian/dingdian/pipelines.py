# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DingdianPipeline(object):
    flag = 1

    def __init__(self):
        # 以append打开文件，文件存在则清空
        with open('dingdian.txt', 'a', encoding='utf-8') as self.f:
            if self.flag == 1:
                self.f.truncate()
                self.f.seek(0)
                self.flag = 0

    def process_item(self, item, spider):
        novel_names = item['novel_name']
        novel_urls = item['novel_url']
        print("is writing.......")
        self.f.write(novel_names + ':' + novel_urls + '\n')
        return item
