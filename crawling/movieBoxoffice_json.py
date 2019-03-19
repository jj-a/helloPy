# 영화 일별 박스오피스 수집 - json 파서

# 태그객체 접근
# : 태그객체 = soup.select_one(CSS Selector)

import json

text = '''
{
    "boxOfficeResult":{
        "boxofficeType":"일별 박스오피스",
        "showRange":"20180220~20180220",
        "dailyBoxOfficeList":[
            {
                "rank":"1",
                "rankOldAndNew":"OLD",
                "movieCd":"20170561",
                "movieNm":"블랙 팬서",
                "salesAmt":"1339822000",
                "audiCnt":"171158"
            },
        {
                "rank":"2",
                "rankOldAndNew":"OLD",
                "movieCd":"20168250",
                "movieNm":"골든슬럼버",
                "salesAmt":"363771900",
                "audiCnt":"48097"
            }
        ]
    }
}
'''
#print(text)

d = json.loads(text) #JSON 파서

for record in d['boxOfficeResult']['dailyBoxOfficeList']:
    print(record['rank'], record['rankOldAndNew'], record['movieCd'], record['movieNm'], record['salesAmt'], record['audiCnt'])

'''
1 OLD 20170561 블랙 팬서 1339822000 171158
2 OLD 20168250 골든슬럼버 363771900 48097
'''
