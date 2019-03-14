# 네이버 실시간 검색어 (1~20위) - CSV 저장

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame,Series

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'https://www.naver.com/'
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text,'html.parser')

columns = ['rank','search_word']
df = DataFrame(columns=columns)
for li in soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li'):
    rank = li.a.select_one('span.ah_r').text
    search_word = li.a.select_one('span.ah_k').text
    print(rank, search_word)
    df = df.append(Series([rank, search_word], index=columns), ignore_index=True)

df.to_csv(r'result.csv', index=False, encoding='utf-8')
