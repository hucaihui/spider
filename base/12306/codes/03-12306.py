#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import json
from selenium import webdriver
from selenium.webdriver import ActionChains

from YDMHTTP import decode

# 导入图片操作对象模块
from PIL import Image
from io import BytesIO


# 导入等待对象模块
from selenium.webdriver.support.wait import WebDriverWait
# 导入条件判断模块
from selenium.webdriver.support import expected_conditions as EC
# 导入查询元素模块
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('./chromedriver')


linktypeid = "dc"
fs = "上海,SHH"
ts = "广州,GZQ"
date = "2019-02-10"
flag = "N,N,Y"

base_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid={}&fs={}&ts={}&date={}&flag={}"
url = base_url.format(linktypeid,fs,ts,date,flag)
browser.get(url)

wait = WebDriverWait(browser,10,0.5)

# 通过时间判定选择点击预订
# 寻找 tr 标签中 属性id值以 ticket_ 开头的数据
tr_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//tr[starts-with(@id,"ticket_")]')))

for tr in tr_list:
    date_string = tr.find_element_by_class_name("start-t").text

    # 判断时间是否在符合条件的范围内
    tr.find_element_by_class_name('btn72').click()
    break

# 点击账号(注意因为是异步加载的所有需要显性等待)
wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"账号登录"))).click()

# 输入用户名和密码
with open('account.json','r',encoding='utf-8') as f:
    account = json.load(f)
browser.find_element_by_id("J-userName").send_keys(account["username"])
browser.find_element_by_id('J-password').send_keys(account["pwd"])


# 获取全屏图片
full_img_data = browser.get_screenshot_as_png()

# 计算截图位置
# 获取截图元素对象
login_img_element = browser.find_element_by_id('J-loginImg')

# 在mac系统下 在retina屏幕下 屏幕中的一个点作为2个像素，location 和 size 属性是根据屏幕点的计算
scale = 2.0
x1 = login_img_element.location["x"] * scale
y1 = login_img_element.location["y"] * scale
x2 = x1 + login_img_element.size["width"] * scale
y2 = y1 + login_img_element.size["height"] * scale

cut_info = (x1,y1,x2,y2)

# 通过计算出的截图图位置在全屏图片中截取所需要的图片
# 把全屏图片构建成全屏图片操作对象
full_img = Image.open(BytesIO(full_img_data))
# 通过截图信息对象截图图片
cut_img = full_img.crop(cut_info)
# 把图片保存到本地
cut_img.save('cut_img.png')

# 发送打码平台获取数字
result = decode('cut_img.png',codetype=6701)
print(result)

# 定义8个点击坐标点
positions = [
    (80,140),
    (230,140),
    (380,140),
    (530,140),
    (80, 280),
    (230, 280),
    (380, 280),
    (530, 280)
]

# 模拟点击坐标
for num in result:
    position = positions[int(num) - 1]
    # ActionChains 动作对象
    ActionChains(browser).move_to_element_with_offset(login_img_element,position[0] / 2,position[1] / 2).click().perform()

# 点击登录
browser.find_element_by_id('J-login').click()

# 点击选择人物
wait.until(EC.visibility_of_element_located((By.ID,"normalPassenger_0"))).click()

# 点击提交订单
browser.find_element_by_id('submitOrder_id').click()

time.sleep(2)
# 点击确认订单
wait.until(EC.visibility_of_element_located((By.ID,'qr_submit_id'))).click()

time.sleep(5)
browser.quit()