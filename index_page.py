#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2020/6/18 22:14
#@Author    :Lyle
#@File      :index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexpage_locators import IndexPageLocators as IL
import random
from Common.basepage import BasePage

class IndexPage(BasePage):


    def isExist_logout_ele(self):
        #如果存在就返回True,如果不存在，就返回False
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@href="/Index/logout.html"]')))
            return True
        except:
            return False
        pass

    #选标操作 --默认选择第一个
    def click_first_bid(self):
        doc="首页_选标操作"
        self.wait_eleVisible(IL.invest_button,doc=doc)
        self.click_element(IL.invest_button,doc)

    #随机选择
    def click_bid_by_random(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((IL.invest_button)))
        #找到所有符合的标
        eles=self.driver.find_elements(*IL.invest_button)
        #随机数据
        index=random.randint(0,len(eles)-1)
        eles[index].click()



