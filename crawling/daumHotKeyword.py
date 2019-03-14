# 다음 실시간 검색어 (1~10위)

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'https://www.daum.net/'
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text,'html.parser')

for li in soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li'):
    rank = li.select_one('span').text
    search_word = li.select_one('span[class="txt_issue"]').text
    print(rank, search_word)
