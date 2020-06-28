#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/18 22:04
#@Author    :Lyle
#@File      :test_login.py
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
import unittest
from TestData import Common_Datas as CD
from TestData import login_datas as LD
import ddt
import pytest
@ddt.ddt
class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg=LoginPage(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(self):
    #     #前置
    #     self.driver=webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.lg=LoginPage(self.driver)

    def tearDown(self):
        #后置
        self.driver.refresh()

    #正常用例 --登录成功
    @pytest.mark.smoke
    def test_login_2_success(self):
        #步骤
        self.lg.login(LD.success_data['user'],LD.success_data['password'])
        #断言
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    #异常用例--手机号格式不正确（大于11位，小于11位，为空，未在号码段）
    @ddt.data(*LD.phone_data)
    def test_login_0_user_wrongFormat(self,data):
        #步骤  输入手机号格式不正确
        self.lg.login(data['user'],data['password'])
        # 断言
        #登录页面中 --获取提示框的文本内容
        #比对文本内容 与 期望值
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(),data['check'])

    @ddt.data(*LD.pwd_data)
    #异常登录（密码、手机号未注册）
    def test_login_1_wrongPwd_noReg(self,data):
        #步骤  输入手机号格式不正确
        self.lg.login(data['user'],data['password'])
        #断言
        self.assertEqual(self.lg.get_errorMsg_from_pageCenter(),data['check'])

    # if __name__ == '__main__':
    #     unittest.main()