#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/26 21:52
#@Author    :Lyle
#@File      :bid_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.bidpage_locators import BidPageLocators as BL
from Common.basepage import BasePage


class BidPage(BasePage):



    #投资
    def invest(self,amount):
        #在输入框 输入金额
        doc="标详情页面_投资操作"
        self.wait_eleVisible(BL.Amount_input_box,doc=doc)
        self.input_text(BL.Amount_input_box,amount,doc)
        #点击投标按钮
        self.click_element(BL.invest_button,doc)

    #获取余额
    def get_user_money(self):
        doc="标详情页面_获取余额"
        self.wait_eleVisible(BL.user_money,doc=doc)
        self.get_element_attribute(BL.user_money,"data_amount",doc)


    #投资成功提示框--点击查看并激活
    def click_activeButton_on_success_popup(self):
        doc="标详情页面_点击查看并激活"
        self.wait_eleVisible(BL.active_button_on_successPop,doc=doc)
        self.click_element(BL.active_button_on_successPop,doc)

    #投资错误提示框--页面中间
    def  get_errorMsg_from_pageCenter(self):
        #获取文本内容
        #关闭提示框
        doc="标详情页面_错误信息页面中间"
        self.wait_eleVisible(BL.invest_faile_popup,doc,doc=doc)
        msg=self.get_text(BL.invest_faile_popup,doc)
        self.click_element(BL.invest_close_failed_popup_button,doc)
        return msg

    #获取提示信息--投标按钮上的关闭操作
    def get_errorMsg_from_investButton(self):
        pass