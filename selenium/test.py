from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoAlertPresentException
import time
web = webdriver.Chrome('/Users/sysner04/Desktop/python/selenium/chromedriver')

web.get('https://cafe.naver.com/ampedbp')

input("키를 입력하면 다음 :")

web.execute_script('writeBoard()')

iframe_src = web.find_element_by_id('cafe_main').get_attribute('src')
new_src = 'http://cafe.naver.com/' + iframe_src.replace('menuid=', 'menuid=14').replace('http://cafe.naver.com/', '')
web.get(new_src)
print(new_src)

time.sleep(1)

try:
    web.switch_to_alert().accept()
    print('1')
except NoAlertPresentException as e:
    print("no alert")
print('2')

# try:
#     web.switch_to_alert().accept()
# except :
#     print('3')
web.find_element_by_id('subject').send_keys('안녕하세요 글쓰기 테스트 입니다.') # 제목
web.switch_to.frame('frame')
# print(web.page_source)
web.find_element_by_tag_name('body').click()
web.find_element_by_tag_name('body').send_keys('안녕하세요 글쓰기 테스트 입니다.')

web.switch_to.default_content()
print(web.page_source)
# print(web.find_element_by_id('cafewritebtn'))

web.execute_script('scroll(0, 100000);')

print(web.find_elements_by_css_selector('.btn_cell a')[0].text)
web.find_elements_by_css_selector('.btn_cell a')[1].click()