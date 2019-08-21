#coding=utf-8
import requests

url = "http://www.baidu.com"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}

response = requests.get(url, headers=headers, timeout=3)

# 获取网页html字符串
print(response.text)  # 乱码，需解码
response.encoding = 'utf-8'
print(response.text)

# 把响应的二进制字节流转化为str类型
print(response.content.decode())

# 获取网页源码
'''
response.content.decode()
response.content.decode("gbk")
response.text()
'''