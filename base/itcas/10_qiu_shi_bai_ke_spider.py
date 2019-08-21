from lxml import html
import requests
import json


class QiuShiBaiKe:
    '''
    #1 根据url地址的规律，构造url地址
    #2 发送请求，获取响应
    #3 提取数据
    #4 保存
    '''

    def __init__(self):
        self.flag = 1
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.url_temp.format(i) for i in range(1, 14)]
        # print(url_list)
        return url_list

    def parse_url(self, url):
        print("now parsing:", url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html_tmp = html.etree.HTML(html_str)
        div_list = html_tmp.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//h2/text()")[0].strip() if len(
                div.xpath(".//h2/text()")[0]) > 0 else None
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.strip("\n") for i in item["content"]]  # 去\n
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"] if len(item["stats_vote"]) > 0 else None
            item["stats_comments"] = div.xpath(".//span[@class='stats-comments']//i/text()")
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):  # 保存
        with open("qiushibaike.txt", "a", encoding='utf-8') as f:  # 以追加模式打开文件
            if self.flag == 1:  # 若文件存在，则清空
                f.seek(0)
                f.truncate()
                self.flag = 0
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        # 1 根据url地址的规律，构造url地址
        url_list = self.get_url_list()
        # 2 发送请求，获取响应
        for url in url_list:
            # 3 提取数据
            html_str = self.parse_url(url)
            conten_list = self.get_content_list(html_str)
            # 4 保存
            self.save_content_list(conten_list)
        print("run over")


if __name__ == "__main__":
    qiushibaike = QiuShiBaiKe()
    qiushibaike.run()
