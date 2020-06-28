#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/26 20:58
#@Author    :Lyle
#@File      :test_invest.py


#前置条件
# 1.用户已登录
# 2.有能够投资的标  #如果没有标，则先加标
# 3.用户有余额可以投资

#步骤
#1.在首页选择标的投资--部根据标名 根据抢投标，默认第一个标
#表页面--获取一个投资前的用户余额
#2.标页面-输入投资金额，点击投资按钮
#3.标页面-点击投资成功的弹出框--查看并激活，进入个人页面

#断言
#钱 投资后的金额，是不是少了投资的量
#个人页面--获取投资后的金额
#投资前的金额-投资后的金额==投资金额

#异常用例：全投操作  标的可投》个人余额
import unittest
import logging
from selenium import webdriver
from TestData import Common_Datas as CD
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from TestData import invest_datas as ID
from PageObjects.user_page import UserPage

class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.info("=====用例类前置：初始化浏览器会话=======")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.web_login_url)
        LoginPage(cls.driver).login(CD.user,CD.password)
        IndexPage(cls.driver).click_first_bid()
        cls.bid_page=BidPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        logging.info("====用例后置：关闭浏览器会话，清理环境====")
        cls.driver.quit()



    def tearDown(self):
        self.driver.refresh()

    def test_invest_success(self):
        logging.info("=====投资用例：正常场景-投资成功=====")
        # 步骤
        # 1.在首页选择标的投资--部根据标名 根据抢投标，默认第一个标
        # 表页面--获取一个投资前的用户余额
        userMoney_beforeInvest=self.bid_page.get_user_money()
        # 2.标页面-输入投资金额，点击投资按钮
        self.bid_page.invest(ID.success['money'])
        # 3.标页面-点击投资成功的弹出框--查看并激活，进入个人页面
        self.bid_page.click_activeButton_on_success_popup()
        # 断言
        # 钱 投资后的金额，是不是少了投资的量
        # 个人页面--获取投资后的金额
        userMoney_afterInvest=UserPage(self.driver).get_user_leftMoney()
        # 投资前的金额-投资后的金额==投资金额
        assert ID.success["money"]==int(float(userMoney_beforeInvest)-float(userMoney_afterInvest))

    def test_invest_failed_no100(self):
        pass

    def test_invest_failed_no10(self):
        pass







