# 영화 일별 박스오피스 수집 - xml 파서

# 태그객체 접근
# : 태그객체 = soup.select_one(CSS Selector)

from bs4 import BeautifulSoup

text = '''
<boxOfficeResult>
<boxofficeType>일별 박스오피스</boxofficeType>
<showRange>20180220~20180220</showRange>
<dailyBoxOfficeList>
<dailyBoxOffice>
<rank>1</rank>
<rankOldAndNew>OLD</rankOldAndNew>
<movieCd>20170561</movieCd>
<movieNm>블랙 팬서</movieNm>
<salesAmt>1339822000</salesAmt>
<audiCnt>171158</audiCnt>
</dailyBoxOffice>
<dailyBoxOffice>
<rank>2</rank>
<rankOldAndNew>OLD</rankOldAndNew>
<movieCd>20168250</movieCd>
<movieNm>골든슬럼버</movieNm>
<salesAmt>363771900</salesAmt>
<audiCnt>48097</audiCnt>
</dailyBoxOffice>
</dailyBoxOfficeList>
</boxOfficeResult>
'''

### ERROR ###
soup = BeautifulSoup(text, 'lxml-xml')  # XML 파서

boxofficeType = soup.select_one('boxofficeType')
print(boxofficeType)  # <boxofficeType>일별 박스오피스</boxofficeType>
print(boxofficeType.text)  # 일별 박스오피스
print(type(boxofficeType))  # <class 'bs4.element.Tag'>

showRange = soup.select_one('showRange')
print(showRange)  # <showRange>20180220~20180220</showRange>
print(showRange.text)  # 20180220~20180220
print(type(showRange))  # <class 'bs4.element.Tag'>
