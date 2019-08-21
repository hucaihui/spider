
# 1、scrapy参考
[Scrapy从安装到实战框架爬虫Demo](https://blog.csdn.net/qq_34532187/article/details/82934538)

[小白进阶之Scrapy第一篇-崔静才](https://cuiqingcai.com/3472.html)

[pipline保存文件](https://www.cnblogs.com/cnkai/p/7397421.html)

# 2、文件说明
**dingdian** 示例

**scrapyBron.bat**
用于生成一个\*run.py文件（Scrapy默认是不能在IDE中调试的）
```
echo execute(['scrapy','crawl','%spiderName%'])>>%spiderName%Run.py
echo #execute(['scrapy','crawl','%spiderName%','-o','%spiderName%.json'])>>%spiderName%Run.py
```

