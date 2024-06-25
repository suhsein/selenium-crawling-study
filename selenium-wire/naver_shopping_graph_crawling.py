# 셀레늄 와이어 웹드라이버
from seleniumwire import webdriver

# 디코딩
from seleniumwire.utils import decode
# 옵션
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import json
# #############################################################

custom_option = Options()

browser = webdriver.Chrome(options=custom_option)
browser.maximize_window()

URL = 'https://datalab.naver.com/shoppingInsight/sCategory.naver'
browser.get(URL)
browser.implicitly_wait(10)


#############################################################

browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/a').click()
time.sleep(2)

for request in browser.requests:
    if str(request) == 'https://datalab.naver.com/shoppingInsight/getCategoryClickTrend.naver':
        # print(request.response.body)

        # 디코딩
        decodeData = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')).decode('utf-8')
        print(decodeData)

        # json 형식으로 변환
        jsonData = json.loads(decodeData)