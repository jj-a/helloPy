# 영화 일별 박스오피스 수집

# Site :  http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do
# key :  b27eaad5245aaa17c169ac8adf18f5f1
# Menual : http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

# 수집할 데이터 #
# rank (순위)
# rankOldAndNew (신규진입여부)
# movieCd (영화코드)
# movieNm (영화명)
# salesAmt (매출액)
# audiCnt (관객수)

import requests
import json

key = 'b27eaad5245aaa17c169ac8adf18f5f1'
date = 20190312  # 어제 이전 날짜까지만 설정 가능
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=' + key + '&targetDt=' + str(date)
res = requests.get(url)
text = res.text
# print(text)

# JSON 데이터 수집
d = json.loads(text)
# print(d)

print('*', date,  '박스오피스 정보', '*')
print('순위/신규진입여부/영화코드/영화명/매출액/관객수')

for b in d['boxOfficeResult']['dailyBoxOfficeList']:
    print(b['rank'], b['rankOldAndNew'], b['movieCd'], b['movieNm'], b['salesAmt'], b['audiCnt'])

