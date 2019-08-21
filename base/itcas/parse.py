import requests
from retrying import retry

headers_computer = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
headers_mobie = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Referer": "https://m.douban.com/tv/american"
}
'''
专门请求url地址的方法
'''


@retry(stop_max_attempt_number=3)  # 让被装饰的函数反复执行3次，3次全报错才报错
def _parse_url(url):
    # print("*"*100)
    response = requests.get(url, headers=headers_mobie, timeout=3)
    return response.content.decode()


def parse_url(url):
    # noinspection PyBroadException
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url1 = "http://www.baidu.com"
    print(parse_url(url1)[:200])
