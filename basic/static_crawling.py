import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve


'''
정적 크롤링 
-> 로그인, 버튼클릭, 키입력 등의 동적 요소가 필요없는 크롤링을 의미한다.

정적 크롤링의 경우 브라우저 없이도 서버상에서 http 호출을 통해 데이터를 가져온다. 
'''

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%90%EC%9D%B4%ED%8B%B0%EC%A6%88'

response = requests.get(url)

# requests 라이브러리를 사용하여 HTTP 요청을 보내 HTML 문서를 크롤링한 것으로, 단순한 `text`에 지나지 않는다. 
html_text = response.text

'''
beautifulsoup의 생성자를 사용하여 `의미있는 HTML 문서`로 변환한다.(파싱) 
html.parser 사용할 수도 있으나, lxml 과 같은 c언어로 작성된 외부 라이브러리 사용 가능
c언어는 컴파일러 언어, 파이썬은 인터프리터 언어로 속도면에서 c언어가 더 좋음 => lxml이 더 빠르다. (단 의존성 추가가 필요함)
'''
html = bs(html_text, 'lxml')
## print(html)


'''
중요
정적 웹 크롤링의 핵심이라고 볼 수 있는 부분이다. 

find -> 직관적이지는 않음
select -> 직관적임
'''

news_titles = html.select('a.news_tit')

# 이름 추출 get_text()
for i in news_titles:
    i = i.get_text()
    print(i)

# 링크 추출 attrs['href']
for i in news_titles:
    href = i.attrs['href']
    print(href)


# 이미지 추출 attrs['src']
news_content_div = html.select('.news_contents')
news_thumbnail = [thumbnail.select_one('.thumb') for thumbnail in news_content_div]
link_thumbnail = []

for img in news_thumbnail :
    if img is not None and 'data-lazysrc' in img.attrs:
        link_thumbnail.append(img.attrs['data-lazysrc'])


path_folder = '/Users/user1/Desktop/img/'

if not os.path.isdir(path_folder) :
    os.makedirs(path_folder)


# urlretrieve로 해당 경로의 파일을 다운로드 받음(파일 경로(url encoded), 로컬 저장경로(이름 포함))
i = 0

for link in link_thumbnail:
    i += 1
    urlretrieve(link, path_folder + f'{i}.jpg')