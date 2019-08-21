import requests
from requests.exceptions import ConnectionError
import re
import pandas as pd
import json
from fun import get_header


headers = get_header()

def get_one_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('err:cannot to connect to ', url)
        return None


def parse_one_page(html):
    #print(html)
    pattern = re.compile('<tbody'
                         '.*?class="number".*?id=\'idUrl(.*?)\'.*?href=\'(https.*?)\'\s'
                         '.*?</tbody>', re.S)
    matchs = re.findall(pattern, html)
    global g_order
    if matchs:
        for match in matchs:
            print('now requests:')
            g_order = match[0]
            yield(match[1])


def parse_next_page(url):
    html = get_one_page(url)
    pattern = re.compile('<tr>'
                         '.*?<span>(.*?)</span>'
                         '.*?<span>(.*?)</span>'
                         '.*?</tr>', re.S)
    matchs = re.findall(pattern, html)
    values = re.findall('"_BLANK">.*?(\d+).*?</a>', html, re.S)

    for match in matchs:
        content = {'order':g_order,'value':values[0],'GCA':match[0],'card':match[1]}
        print(content)
        write_to_csv(content)


def write_to_csv(content):
    df = pd.DataFrame({key:value for key,value in content.items()},index=[0])
    df.to_csv('pgczk.csv', mode='a', sep=',',header=False)
    # df.to_excel('pgczk.xls')

def write_to_txt(content):
    with open('pgczk.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(d, page):
    url = 'https://order.jd.com/center/list.action?d='+str(d)+'&s=4096&page='+str(page)
    print(url)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        parse_next_page(item)


if __name__ == '__main':

    d = 1  # d=1 近三个月内订单，d=2 今年内订单...
    pagesNum = 1  # 需要爬取的订单总页数
    for page in range(1, pagesNum+1):
        main(d, page)


