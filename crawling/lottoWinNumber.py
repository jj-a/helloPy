# 나눔로또 당첨 결과

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
res = requests.get(url, headers=headers)
text = res.text
soup = BeautifulSoup(text, 'html.parser')

items = soup.select('div.content_wrap.content_winnum_645 > div.win_result > div.nums > div.num.win > p > span')

winballs = []
for i in items:
    winballs.append(i.text)

bonus = soup.select_one('div.content_wrap.content_winnum_645 > div.win_result > div.nums > div.num.bonus > p > span').text

print("최근 로또 번호 당첨 결과: ")
for i in winballs:
    print(i)
print("보너스:", bonus)
