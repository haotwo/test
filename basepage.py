#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/27 21:23
#@Author    :Lyle
#@File      :basepage.py
import logging
import datetime
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.dir_config import *
#封装基本函数  执行日志  异常处理 失败截图
#2. 所有的页面公共的部分
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,wait_times=30,poll_frequency=0.5,doc=""):
        """

        :param locator: 元素定位 ，元素形式（元素定位类型、元素定位方式）
        :param times:
        :param poll_frequency:
        :param doc:   模块名
        :return:
        """
        logging.info("等待元素{0}可见".format(locator))
        try:
            #开始等待时间
            start=datetime.datetime.now()
            WebDriverWait(self.driver,wait_times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束时间
            end=datetime.datetime.now()
            wait_times=(end-start).seconds
            #求一个差值
            logging.info("{0}:元素{1}已可见，等待起始时间:{2},等待结束时间:{3}.等待时间{4}".format(doc,locator,start,end,wait_times))

        except:
            logging.exception("等待元素可见失败！！！！")
            self.save_screenshot(doc)
            raise
            #截图操作
    #等待元素存在
    def wait_elePresence(self):
        pass

    #查找元素
    def get_element(self,locator,doc=""):
        logging.info("查找元素:{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！！")
            self.save_screenshot(doc)
            raise
        pass

    #点击操作
    def click_element(self,locator,doc=""):
        #找元素
        ele=self.get_element(locator,doc)
        #元素操作
        logging.info("{0}点击元素:{1}".format(doc,locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击失败！！！")
            #截图
            self.save_screenshot(doc)
            raise
        pass

    #输入操作
    def input_text(self,locator,text,doc=""):
        #找元素
        ele=self.get_element(locator,doc)
        try:
            ele.send_keys(text)
        except:
            logging.exception("文本输入失败！！！")
            #截图
            self.save_screenshot(doc)
            raise


    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.exception("文本获取失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("元素属性获取失败！！！")
            self.save_screenshot(doc)
            raise


            #alert处理
    def alert_action(self,action="accept"):
        pass

    #iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    #上传操作
    def upload_file(self):
        pass

    #滚动条处理
    #窗口切换

    #截图操作
    def save_screenshot(self,doc):
        #图片名称：模块名_页面名称_操作名称_时间(年月日 时分秒).png
        #当前时间
        filePath=screenshot_dir + \
                  "/{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为：{}".format(filePath))
        except:
            logging.exception("截图失败")


