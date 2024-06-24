# 셀레늄 웹드라이버
from selenium import webdriver

# 웹드라이버 객체 생성시 수반될 서비스나 옵션
## from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 선택자 및 키보드 입력
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

##########################################################

import time

# 엑셀 저장
import openpyxl

##########################################################

'''
동적 크롤링의 경우 로그인, 버튼클릭, 키입력 등이 필요한 크롤링이다.
대부분 실행 시 브라우저를 켜서 진행하게 된다.
'''

# 옵션 변수
customOption = Options()

# 드라이버 객체 생성
browser = webdriver.Chrome(options=customOption)

# 전체 화면. 전체 화면이 아닐 경우 요소를 찾지 못해서 오류 발생
browser.maximize_window()


URL = 'https://www.naver.com'
browser.get(URL)
browser.implicitly_wait(10) # -> 해당 URL의 웹 페이지가 로딩되기까지 최대 10초간 기다림 (그 전에 로딩되면 기다리지 않음)

## time.sleep(3)  # -> implicitly_wait() 과 달리 입력한 시간만큼 모두 기다림

'''
자바스크립트 값이나 css 값도 크롤링을 위해서 많이 사용되지만, 셀레늄에서는 주로 XPath를 사용함.

XPath 
-> 셀레늄에서 접근하게 될 요소의 실제 위치를 의미함(데이터 획득, 버튼 클릭을 위해 사용됨)
-> HTML 문서 요소들을 계층 구조로 나열했을 때, 원하는 요소의 위치이다.  /로 계층 구분, 전체 경로

획득방법
: 개발자 도구로 원하는 요소를 선택 후, copy XPath로 획득할 수 있음
'''

# find_element() 첫번째 파라미터는 방식을, 두번째 파라미터는 경로 혹은 선택자

# 메일 값
temp = browser.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[1]/a/span[2]').text
print(temp)

# 메일 값 상위 레벨 -> 상위 레벨로도 텍스트 출력 가능
temp = browser.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[1]').text
print(temp)

# send_keys
browser.find_element(By.XPATH, '//*[@id="query"]').send_keys('aaaaa')
time.sleep(5)

# 버튼 클릭
browser.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
time.sleep(3)


