# 영화 상세정보 수집

# Site :  http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do
# key :  b27eaad5245aaa17c169ac8adf18f5f1
# Menual : http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do)

# 수집할 데이터 #
# movieCd (영화코드)
# movieNm (영화명)
# showTm (상영시간)
# actors_count (배우 수) : len(actors), 배우 리스트에서 배우 수
# showTypes_count (상영형태 구분 수) : len(showTypes), 상영형태 구분 리스트에서 상영형태 구분 수

import requests
import json

key = 'b27eaad5245aaa17c169ac8adf18f5f1'
movieCd = 20181877  # 영화코드  # 캡틴 마블

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key='+key+'&movieCd='+str(movieCd)
res = requests.get(url)
text = res.text
#print(text)

d = json.loads(text)
#print(d)

print('* 영화 상세 정보 *')
print('영화코드/영화명/개봉일/관람이용가/장르/국가/상영시간/배우수/상영형태수')

print(d['movieInfoResult']['movieInfo']['movieCd'],
      d['movieInfoResult']['movieInfo']['movieNm'],
      d['movieInfoResult']['movieInfo']['openDt'],
      d['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'],
      d['movieInfoResult']['movieInfo']['genres'][0]['genreNm'],
      d['movieInfoResult']['movieInfo']['genres'][1]['genreNm'],
      d['movieInfoResult']['movieInfo']['genres'][2]['genreNm'],
      d['movieInfoResult']['movieInfo']['nations'][0]['nationNm'],
      d['movieInfoResult']['movieInfo']['showTm'],
      len(d['movieInfoResult']['movieInfo']['actors']),
      len(d['movieInfoResult']['movieInfo']['showTypes']))

