import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import re
import json
from multiprocessing import Pool
import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]


def get_one_page(start):
    data = {
        'type': 5,
        'interval_id': '100:90',
        'action': "",
        'start': start,
        'limit': '20'
    }
    url = 'https://movie.douban.com/j/chart/top_list?' + urlencode(data)
    print("is runing url:",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("error:cannot to requset index page ")
        return None


def parse_page_index(html):
    data = json.loads(html)
    for item in data:
        # print(item['url'])
        yield item['url']


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("error:cannot to requset detail page ")
        return None


def parse_page_detail(html):
    pattern = re.compile('v:itemreviewed">(.*?)</span>'
                         '.*?v:average">(.*?)</strong>'
                         '.*?v:votes">(\d+)</span>'
                         '.*?stars5.*?rating_per">(.*?)</span>'
                         '.*?stars4.*?rating_per">(.*?)</span>'
                         '.*?stars3.*?rating_per">(.*?)</span>'
                         '.*?stars2.*?rating_per">(.*?)</span>'
                         '.*?stars1.*?rating_per">(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'name': item[0],
            'score': item[1],
            'people': item[2],
            'start5': item[3],
            'start4': item[4],
            'start3': item[5]
        }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        #print("insert to mongdb success", result)
        return True
    return False


def main(offset):
    html = get_one_page(offset)
    for url in parse_page_index(html):
        html_detail = get_page_detail(url)
        items = parse_page_detail(html_detail)
        for item in items:
            print(item)
            save_to_mongo(item)


if __name__ == "__main__":
    # main()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool()
    pool.map(main, groups)
