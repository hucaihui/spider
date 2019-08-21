#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

# 1. 导入模块
from selenium import webdriver

# 导入等待对象模块
from selenium.webdriver.support.wait import WebDriverWait
# 导入条件判断模块
from selenium.webdriver.support import expected_conditions as EC
# 导入查询元素模块
from selenium.webdriver.common.by import By

# 2. 通过驱动创建浏览器对象
# 创建浏览器对象 2 种方式
# 2.1> 参数需要指定驱动路径（推荐使用这种方案）
browser = webdriver.Chrome('./chromedriver')

# 设置隐性等待
# browser.implicitly_wait(5)

# 2.2> PATH 全局的环境变量，可以把驱动文件拷贝到 $PATH 路径中
# browser = webdriver.Chrome()

# 3. 输入网址
browser.get('https://www.baidu.com')

# 4. 操作浏览器
'''
find 系列函数，专门用于定位元素

find_element_by_xxx         寻找符合条件的第一个元素
find_elements_by_xxx        寻找符合条件的所有元素（返回是一个列表）

by_xxx 
find_element(s)_by_class_name  可以通过 class_name 寻找元素
find_element(s)_by_id
find_element(s)_by_name
find_element(s)_by_tag_name
find_element(s)_by_css_selector
find_element(s)_by_link_text           通过文本内容寻找元素
find_element(s)_by_partial_link_text   通过包含某个内容寻找元素
find_element(s)_by_xpath               通过 xpath 寻找元素
'''
# print(browser.find_elements_by_link_text("新闻"))
# print(browser.find_elements_by_partial_link_text("频"))

# 获取元素文本内容
# print(browser.find_element_by_class_name("mnav").text)
# 获取元素的属性
# print(browser.find_element_by_class_name('mnav').get_attribute("href"))

# 获取元素属性
# print(browser.find_element_by_name("wd").send_keys("黑马程序员"))

# 补充,让元素点击,模拟元素点击
# browser.find_element_by_id('su').click()



# 4.1 输入关键词
input_element = browser.find_element_by_id("kw")
input_element.send_keys("itcast")

# 4.2 点击百度一下
button_element = browser.find_element_by_id('su')
button_element.click()

# time.sleep(2)

# 4.3 找到传智播客连接并且打开

# 显性等待，每个元素都可以自己定义检查条件
'''
timeout = 60

t = time.time()

while True:
    try:
        # 检测时间间隔
        time.sleep(0.1)

        link_element = browser.find_element_by_class_name("favurl")
        link_element.click()
        break
    except:
        # 超时设置
        if time.time() - t > timeout:
            break
        pass
'''

# 系统提供显性等待API
# 1. 创建等待对象
# 第一个参数浏览器对象
# 第二个参数是超时时间
# 第三个参数检测时间间隔
wait = WebDriverWait(browser,5.0,0.5)

# 2. 通过等待对象获取元素
# presence_of_element_located 检查元素是否存在，如果存在就返回如果不存在就继续检查
# visibility_of_element_located 检查元素是否可见
link_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"favurl")))
link_element.click()


time.sleep(5)

# 5. 退出浏览器
browser.quit()
