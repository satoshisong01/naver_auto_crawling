from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import time

#에러주소 https://cafe.naver.com/spongerice?iframe_url=%2Fca-fe%2Fcafes%2F10914089%2Fmenus%2F3%2Farticles%2Fwrite-error
#스펀지밥 주소 https://cafe.naver.com/ca-fe/cafes/10914089/menus/3/articles/write?boardType=L
#팩토리 주소 https://cafe.naver.com/ca-fe/cafes/30490614/menus/1/articles/write?boardType=L
#팩토리 댓글주소 https://cafe.naver.com/factory1.cafe?iframe_url=/CafeMemberNetworkView.nhn%3Fm=view%26memberid=5143862k

# '#tournament-page-results-more > tbody > tr > td > a' 태그 참조 정석

driver = webdriver.Chrome('/Users/sysner04/Desktop/python/selenium/chromedriver')
url = "https://cafe.naver.com/ca-fe/cafes/30490614/menus/1/articles/write?boardType=L"
driver.get(url)
action = ActionChains(driver)

#then = datetime(2021, 7, 16, 21, 0, 20) 팩토리 시간
yoon1 = "팩토리 !"
yoon2 = "팩토리 짱짱맨!"
driver.implicitly_wait(15)
time.sleep(13)

print("----------")
print("----2-----")
while True:
    now = datetime.now()
    print(now.hour,"시",now.minute,"분",now.second,"초 main")
    time.sleep(0.7)
    if (now.hour == 21 and now.second > 0) or (now.hour == 20 and now.minute == 59 and now.second > 50):
        if driver.current_url != url:
            driver.get(url)
            print("주소가 달라서 리프뤠쉬~")
        else:    
            action.send_keys(yoon2).perform() #내용 입력
            time.sleep(0.2)
            action.send_keys(yoon2).perform()
            driver.find_element_by_css_selector(".textarea_input").send_keys(yoon1)
            driver.find_element_by_css_selector(".BaseButton").click()