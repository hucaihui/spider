:: scrapy startprojecect <fileName>
:: scrapy genspider <spiderName> <allowed_domains>
:: scrapy crawl <spiderName> 
:: scrapy crawl <spiderName> -o <saveFileName>   spiderName.json...
@echo off
@title 快速生成scrapy项目、spiderName文件以及Run.py文件

@echo ----input the fileName:
set/p fileName=
if not exist %fileName% (
	scrapy startproject %fileName%
	@echo   Retsultsult:the %fileName% is create success 
)

cd/d %fileName%

@echo ----input the spiderName:
set/p spiderName=
@echo ----input the allowed_domains:
set/p allowed_domains=
scrapy genspider %spiderName% %allowed_domains%
@echo   Retsult:the %spiderName%.py is create success 

echo from scrapy.cmdline import execute>%spiderName%Run.py
echo execute(['scrapy','crawl','%spiderName%'])>>%spiderName%Run.py
echo #execute(['scrapy','crawl','%spiderName%','-o','%spiderName%.json'])>>%spiderName%Run.py
@echo  %spiderName%Run.py is create success

cd/d E:\pycharm\PyCharm Community Edition 2018.2.4\bin
start pycharm.exe


pause