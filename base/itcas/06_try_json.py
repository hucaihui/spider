import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36"}

url = "https://fanyi.baidu.com/basetrans"
query_str = input("请输入要翻译的中文：")
post_data = {"query": query_str,
             "from": "zh",
             "to": "en"}

response = requests.post(url, data=post_data, headers=headers)
html_str = response.content.decode()  # json字符串
# print(html_str)
# print("*"*100)
dict_ret = json.loads(html_str)  # json字符串  ->  dict型
# print(dict_ret)
print("*" * 100)
# print(dict_ret["trans"])
# print(dict_ret["trans"][0])
# print(dict_ret["trans"][0]["dst"])
ret = dict_ret["trans"][0]["dst"]
print("翻译结果:", ret)
