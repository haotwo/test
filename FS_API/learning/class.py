# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2020/4/21 14:35
#文件 :class.py


# from selenium import webdriver
# import time
# dr=webdriver.Chrome()
#
# dr.get("http://t.qq.com/")
# dr.maximize_window()
# time.sleep(2)
# dr.switch_to.frame('login_div')
# dr.find_element_by_xpath('//*[@id="bottom_qlogin"]/a[2]').click()
# time.sleep(3)
# dr.quit()


from selenium import webdriver
import time as t

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('http://t.qq.com/')
dr.implicitly_wait(10)  # 隐形等待 10秒
print('get_weibo_title:{0}'.format(dr.title))
# 获取腾讯微博页面的标题
t.sleep(1)
JB = dr.current_window_handle
# 获取当前登录页窗口的句柄
print('当前登录页窗口句柄:',JB)
t.sleep(5)
dr.switch_to.frame('login_div')
# 进入frame页面内
t.sleep(3)
dr.find_element_by_xpath('//*[@id="bottom_qlogin"]/a[2]').click()