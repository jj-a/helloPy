# 네이버 실시간 검색어 (1~20위)

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'https://www.naver.com/'
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text, 'html.parser')

for li in soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li'):
    rank = li.a.select_one('span.ah_r').text
    search_word = li.a.select_one('span.ah_k').text
    print(rank, search_word)

