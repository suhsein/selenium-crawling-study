from selenium import webdriver

from selenium.webdriver.chrome.options import Options

###########################################################

custom_options = Options()

'''
add_argument() 로 옵션 추가하기
'''

# 1. 헤드리스 모드 -> 브라우저 창을 켜지 않고 내부적으로 실행하여 크롤링을 진행한다.
# 개발 단계에서 동작됨을 확인하고 헤드리스 모드로 전환 가능.

custom_options.add_argument('--headless')

# 2. 창 크기 조절 : x, y
custom_options.add_argument('--window-size=x,y')

# 3. 최대화
custom_options.add_argument('--start-maximized')

# 4. f11 풀 스크린 모드
custom_options.add_argument('--start-fullscreen')

# 5. 음소거
custom_options.add_argument('--mute-audio')

# 6. user agent (실행하는 os 종류, 버전, 브라우저 등등의 정보 지정)
custom_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')

# 7. 리눅스 옵션
# 리눅스의 경우 아래 옵션을 추가하지 않으면 오류가 발생할 수 있음
custom_options.add_argument('--headless')
custom_options.add_argument('--no-sandbox')
custom_options.add_argument('--disable-dev-shm-usage')

###########################################################

# 웹드라이버 생성
browser = webdriver.Chrome(opitons=custom_options)