'''
로그인 자동화
드라이버에서 find_element() 에 키를 보내어 로그인을 진행하면,
로봇이 접근함을 감지하고 캡차가 발생한다.

우회
-> execute_script()를 통해서 로그인을 진행해야 한다.
execute_script() 는 파이썬에 키를 직접 넘겨주는 것이 아닌, 브라우저 내에서 자바스크립트로 값을 넘겨준다.
물론 안에는 XPath 가 아니라 자바스크립트 선택자가 들어가야 한다.

브라우저 창을 켜지 않는 headless 모드에서도 잘 동작한다고 한다.
'''
# 웹드라이버
from selenium import webdriver

# 옵션
from selenium.webdriver.chrome.options import Options

# 선택자와 키보드 사용
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#################################################################

# 드라이버 설정
custom_option = Options()
browser = webdriver.Chrome(options=custom_option)
browser.maximize_window()

# 웹페이지 읽어오기
URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
browser.get(URL)
browser.implicitly_wait(10)

#################################################################

# find_element() 사용시 캡챠 발생!
## browser.find_element(By.XPATH, '//*[@id="id"]').send_keys('mini9075')
## time.sleep(1)
## browser.find_element(By.XPATH, '//*[@id="pw"]').send_keys('xpslditkfkdgo')
## time.sleep(1)


# execute_script() 로 로그인 진행하기. XPATH 아닌 자바스크립트의 선택자 사용
browser.execute_script("document.querySelector('#id').value='mini9075'")
time.sleep(1)

browser.execute_script("document.querySelector('#pw').value='xpslditkfkdgo'")
time.sleep(1)

# 로그인 버튼
browser.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(3)


