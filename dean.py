from selenium import webdriver
import time
import os
from dean_find import Process
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
##################模拟登陆
#前面讲的登录过程：直接抓包找到post地址，发送过去即可登陆成功
#现在的登录过程，直接登陆发送post不行，因为表单中有一些数据需要从网页中获取到，例如formhash，那么，现在的登录过程就变成
#了先发送get请求到登陆界面，然后通过xpath,bs获取所需要的表单令牌，然后再发送post请求，开始登陆

class Crawler():

    def __init__(self,address,username,keys,url,path,chrome_options,dir):
        self.address=address
        self.username=username
        self.keys=keys
        self.url=url
        self.path=path
        self.options=chrome_options
        self.dir=dir

    def Mkdir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def spider(self):
        # 创建浏览器对象
        browser = webdriver.Chrome(executable_path=self.path, options=self.options)

        def is_visible(locator, timeout=30):
            try:
                ui.WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
                return True
            except TimeoutException:
                return False

        browser.get(self.url)
        browser.maximize_window()
        # browser.save_screenshot('dean/1.png')
        # time.sleep(2)

        is_visible('//input[@class="btn-submit"]')
        browser.find_elements_by_xpath('//input[@id="username"]')[0].send_keys(self.username)
        browser.find_elements_by_xpath('//input[@id="password"]')[0].send_keys(self.keys)
        browser.find_elements_by_xpath('//input[@class="btn-submit"]')[0].click()
        is_visible('//li[@role="tab"]')
        browser.find_elements_by_xpath('//li[@role="tab"]')[1].click()
        # browser.save_screenshot('dean/3.png')

        # time.sleep(2)
        is_visible('//table[@id="tableqb-index-table"]')

        #已经写入了第一页的数据
        with open(self.address, 'w', encoding='utf-8') as fp:
            fp.write(browser.page_source)
            fp.close()

        #读取页数数据
        page=Process(self.address)
        pages=page.ProNumber()+1
        button = browser.find_elements_by_xpath('//i[@class="iconfont icon-keyboardarrowright"]')
        for i in range(pages):

            time.sleep(2)
            # is_visible('//i[@class="iconfont icon-keyboardarrowright"]')

            #处理不符合要求的元素
            for i in range(len(button)):
                flag=0
                try:
                    button[i].click()
                    flag=1
                except:
                    print('')
                if flag==1:
                    break


            is_visible('//table[@id="tableqb-index-table"]')

            with open(self.address,'a',encoding='utf-8') as fp:
                fp.write(browser.page_source)
                fp.close()




