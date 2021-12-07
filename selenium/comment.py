from selenium import webdriver
from selenium.webdriver.support.select import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

#스펀지밥 주소 https://cafe.naver.com/ca-fe/cafes/10914089/menus/3/articles/write?boardType=L
#팩토리 주소 https://cafe.naver.com/ca-fe/cafes/30490614/menus/1/articles/write?boardType=L
#팩토리 댓글주소 https://cafe.naver.com/factory1.cafe?iframe_url=/CafeMemberNetworkView.nhn%3Fm=view%26memberid=5143862k

driver = webdriver.Chrome('/Users/sysner04/Desktop/python/selenium/chromedriver')
url = "https://cafe.naver.com/spongerice?iframe_url=/CafeMemberNetworkView.nhn%3Fm=view%26memberid=ex_xe%26clubid=10914089"
driver.get(url)
time.sleep(10)
yoon1 = "댓글댓글!"
print(123123)
driver.get(url)
print(driver.find_element_by_css_selector(".inner_number"))


# print(1)
# driver.find_element("avascript:goArcicle(11)")
# print(2)
# driver.find_element_by_css_selector("javascript:goArcicle(11)")
# print(3)
# while True:
#     now = datetime.now()
#     print(now.second)
#     time.sleep(1)
#     if driver.find_element_by_css_selector(".inner_number") > 11:
#         driver.find_element_by_css_selector(".inner_list > a").click()
#         if  now.minute == 26 and now.second > 20:
#             driver.find_element_by_css_selector(".comment_inbox_text").send_keys(yoon1) #댓글입력
#             driver.find_element_by_css_selector(".btn_register").click() #등록
#     else:    
#         driver.get(url)
