import requests

# 先发送pose请求，获取cookie,带上cookie请求登录后的页面

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
}

# 使用session发送Post请求，获取对方保存在本地的cookie
post_url = "http://www.renren.com/PLogin.do"
post_data = {
    "email": "13218343010",
    "password": "A781223439"
}
session = requests.session()
session.post(post_url, headers=headers, data=post_data)
print(session.cookies.get_dict())   # 获得的cookie
# 在使用session 请求登录后的页面
url = "http://www.renren.com/852690845/profile"
response = session.get(url, headers=headers)

with open("renren3.html", "w", encoding='utf-8') as f:
    f.write(response.content.decode())
