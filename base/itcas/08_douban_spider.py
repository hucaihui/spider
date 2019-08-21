from parse import parse_url
import json

# 返回json的数据
'''浏览器切换到手机版
   抓包app
   '''

class DouBanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def get_contentf_list(selfself, html_str):  # 提取数据
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_lis(self, content_list):
        with open("douban.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):  # 主要逻辑
        '''
        # 1 start_url
        # 2 改送请求，获取响应
        # 3 提取数据
        # 4 保存
        # 5 构造下一页的url地址，循环2-5步
        '''
        num = 0
        total = 100
        while num < total + 18:
            # 1 start_url
            start_url = self.temp_url.format(num)
            print(start_url)
            # 2 改送请求，获取响应
            html_str = parse_url(start_url)
            # 3 提取数据
            content_list, total = self.get_contentf_list(html_str)
            print(total)
            # 4 保存
            self.save_content_lis(content_list)
            # 5 构造下一页的url地址，循环2-5步
            num += 18


if __name__ =="__main__":
    douban = DouBanSpider()
    douban.run()
