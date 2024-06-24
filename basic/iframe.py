'''
XPath 찾아서 요소를 찾아도 찾아지지 않는 경우,
해당 요소가 iframe에 담겨져 있는지 확인한다.

이러한 경우에는 해당 요소를 포함하는 iframe으로 전환 후 찾는다.
(이후 다시 되돌리기 필요)
'''
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
###########################################################

# 웹드라이버 생성
browser = webdriver.Chrome()
browser.maximize_window()

URL = 'https://www.naver.com/'
browser.get(URL)
browser.implicitly_wait(10)

'''
iframe 전환

browser.switch_to.frame() 사용

1. iframe의 name 혹은 id
2. 인덱스(0번부터 시작)
3. id나 name 없는 경우, find_element()로 찾아서
'''

# iframe 전환
browser.switch_to.frame(browser.find_element(By.XPATH, '//*[@id="ad_timeboard_tgtLREC"]'))
browser.find_element(By.XPATH, '//*[@id="ac_banner_a"]').click()

# default content 로 되돌리기
browser.switch_to.default_content()

time.sleep(3)

