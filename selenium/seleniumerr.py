from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('/Users/sysner04/Desktop/python/selenium/chromedriver')
url = "https://cafe.naver.com/factory1.cafe?iframe_url=/CafeMemberNetworkView.nhn%3Fm=view%26memberid=5143862k"
yoon1 = "1등인가!??"
driver.get(url)
print("로그인을 15초안에 해주세요")
driver.implicitly_wait(15)
time.sleep(15)
print("-----0-----")
while True:
    time.sleep(0.7)
    now = datetime.now()
    if (now.hour == 21 and now.second > 0) or (now.hour == 20 and now.minute == 59 and now.second > 50):
            print(now.hour,"시",now.minute,"분",now.second,"초")
            driver.refresh()
            driver.switch_to.frame("cafe_main")
            driver.switch_to.frame("innerNetwork")
            if int(driver.find_element_by_css_selector(".inner_number").text) > 2: #인덱스 번호가 더클떄(최신게시물)
                driver.find_element_by_xpath("""//*[@id="main-area"]/div[1]/table/tbody/tr[1]/td[1]/div[2]/div/a""").click() #게시물 클릭
                driver.switch_to.default_content()
                driver.implicitly_wait(5)
                print("-----1-----")
                driver.switch_to.frame("cafe_main")
                driver.implicitly_wait(5)
                print("-----2-----")
                driver.find_element_by_css_selector(".comment_inbox_text").send_keys(yoon1) #덧글작성
                driver.implicitly_wait(5)
                print("-----3-----")
                driver.find_element_by_css_selector(".btn_register").click() #등록
                print("-----4-----")
                break