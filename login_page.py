#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/18 21:55
#@Author    :Lyle
#@File      :login_page.py

from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage
class LoginPage(BasePage):   #继承BsePage类

    def login(self,username,password,rember_user=True):
        #输入用户名
        #输入密码
        #点击登录
        doc="登录页面_登录功能"
        self.wait_eleVisible(loc.login_but,doc=doc)
        self.input_text(loc.name_text,username,doc)
        self.input_text(loc.pwd_text,password,doc)
        self.click_element(loc.login_but,doc)

    #获取错误提示信息--登录区域
    def get_errorMsg_from_loginArea(self):
        doc="登录页面_获取登陆区域的错误提示"
        self.wait_eleVisible(loc.login_errMsg,doc=doc)
        return self.get_text(loc.login_errMsg,doc)

    #获取错误信息--页面正中间
    def get_errorMsg_from_pageCenter(self):
        doc = "登录页面_获取页面正中间的错误提示"
        self.wait_eleVisible(loc.login_errMid,doc=doc)
        return self.get_text(loc.login_errMid,doc)



