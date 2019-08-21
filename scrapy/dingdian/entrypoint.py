from scrapy.cmdline import execute

'''
new add
refer https://cuiqingcai.com/3472.html
scrapy是默认不能调试的
格式  execute(['scrapy', 'crawl', '<filename>'])
'''
execute(['scrapy', 'crawl', 'dingdian'])
