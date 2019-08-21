from lxml import html
import requests

headers_computer = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
url = "https://movie.douban.com/chart"

response = requests.get(url,headers=headers_computer)
html_str = response.content.decode()
# print(html_str)

# 使用
html = html.etree.HTML(html_str)  # <class 'lxml.etree._Element'>
print(html)

# 1 获取所有需要的电影的url地址
url_list = html.xpath("//div[@class='indent']//table//div/a/@href")  # <class 'list'>
# print(url_list)

# 2 所有图片的地址
img_list = html.xpath("//div[@class='indent']//table//td//img/@src")  # <class 'list'>
# print(img_list)

# 3 每部电影组成一个字典，字典中包括标题，url，图片地址，评论数，评分
#节点
ret1 = html.xpath("//div[@class='indent']/div/table")
# print(ret1)

f = open("danban2.csv","w",encoding='utf-8')
for table in ret1:
    item = dict()
    item["title"] = table.xpath(".//td/div/a/text()")[0].replace("/", " ").strip()
    item["href"] = table.xpath(".//td/div/a/@href")
    item["rating_num"] = table.xpath(".//td/div//span[@class='rating_nums']/text()")[0]
    item["commant_num"] = table.xpath(".//td/div//span[@class='pl']/text()")[0].strip("(").strip(")")   # 是PL  不是P1
    item["href"] = table.xpath(".//td/div/a/@href")
    item["img"] = table.xpath(".//img//@src")
    print(item)
    for k, v in item.items():
        f.write(str(v))
        f.write(",")
    f.write("\n")




