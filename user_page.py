#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/26 21:53
#@Author    :Lyle
#@File      :user_page.py
from Common.basepage import BasePage
from PageLocators.userpage_locators import UserPageLocators as UL
class UserPage(BasePage):
    def get_user_leftMoney(self):
        doc="个人中心_获取余额"
        self.wait_eleVisible(UL.get_user_leftMoney,doc=doc)
        msg=self.get_text(UL.get_user_leftMoney,doc)
        return msg
