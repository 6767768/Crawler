from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

#模拟创建浏览器对象，通过对象去操作浏览器
path="G:\chromedriver.exe"
browser=webdriver.Chrome(executable_path=path)
url="http://www.baidu.com/"
browser.get(url)
input=browser.find_element_by_id("kw")
input.send_keys("Python")
input.send_keys(Keys.ENTER)
wait=WebDriverWait(browser,10)
wait.until(EC.presence_of_all_elements_located((By.ID,"content_left")))
# print(browser.current_url)
print(browser.get_cookies())
# print(browser.page_source)
time.sleep(10)
browser.close()




browser.close()