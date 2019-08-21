import requests

url = "https://fanyi.baidu.com/basetrans"

post_data = {"query": "人生苦短",
                "from": "zh",
                "to": "en"}

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36"
    }
response = requests.post(url, data=post_data, headers=headers)
print(response)
response.encoding = "utf-8"
print(response.content.decode())
print(type(response.content.decode()))