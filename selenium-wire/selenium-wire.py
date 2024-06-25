# 셀레늄 와이어(네트워크 패킷 크롤링)
from seleniumwire import webdriver

# 디코딩
from seleniumwire.utils import decode

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#############################################################

# 웹드라이버 생성

# 주의 options != seleniumwire_options
# options: 브라우저의 옵션. Options 객체를 값으로 가짐
# seleniumwire_options: 네트워크 관련 설정을 조정하는데 사용됨. 딕셔너리를 값으로 가짐
custom_options = Options()
browser = webdriver.Chrome(options=custom_options)

browser.maximize_window()

URL = "https://www.naver.com"
browser.get(URL)
browser.implicitly_wait(10)


#############################################################

# 네트워크 패킷 관련 메서드
# 응답받은 데이터에 대해서 디코딩을 진행해야 원본 데이터 획득 가능!


# 요청 헤더 및 바디 조회 메서드
for request in browser.requests:
    print(request)

    print(request.headers)  # 요청 헤더
    print(request.body)  # 요청 바디
    print(request.path)  # 요청 경로
    print(request.querystring)  # 요청 쿼리스트링


# 응답 헤더 및 바디 조회 메서드 (요청-응답 짝)
for request in browser.requests:
    print(request.response)

    print(request.response.headers)  # 응답 헤더
    print(request.response.body)  # 응답 바디
    print(request.response.status_code)  # 응답 코드
