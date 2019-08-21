import json
import requests
# url 中的 callback = json1 需要删除   json.loads才可使用
url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1547777611817"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
    "Referer": "https://m.douban.com/tv/american"
}

response = requests.get(url, headers=headers)

json_str = response.content.decode()

ret1 = json.loads(json_str)
print(ret1)

with open("douban.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
