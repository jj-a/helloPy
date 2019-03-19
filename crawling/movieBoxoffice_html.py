# 영화 일별 박스오피스 수집 - html 파서 1

# 태그객체 접근
# : 태그객체 = soup.select_one(CSS Selector)

from bs4 import BeautifulSoup

text = '''
<html>
<body>
<h1 align="center" id="boxofficeTypeId" class="boxofficeType">일별 박스오피스</h1>
<center>
<h1 id="showRangeId" class="showRange">20180220~20180220</h1>
</center>
<table border="1" align="center">
<tr>
<td class="rank">순위 (rank)</td>    
<td class="rankOldAndNew">신규진입여부 (rankOldAndNew)</td>    
<td class="movieCd">영화코드 (movieCd)</td>    
<td class="movieNm">영화명 (movieNm)</td>  
<td class="salesAmt">매출액 (salesAmt)</td> 
<td class="audiCnt">관객수 (audiCnt)</td> 
</tr>
<tr>
<td class="rank">1</td>   
<td class="rankOldAndNew">OLD</td>   
<td class="movieCd">20170561</td>   
<td class="movieNm">블랙 팬서</td> 
<td class="salesAmt">1339822000</td>   
<td class="audiCnt">171158</td>   
</tr>   
</table>
</body>
</html>
'''

soup = BeautifulSoup(text, 'html.parser') #HTML 파서

##################

#태그
h1 = soup.select_one('h1')
print(h1) #<h1 align="center" class="boxofficeType" id="boxofficeTypeId">일별 박스오피스</h1>
print(h1.text) #일별 박스오피스
print(type(h1)) #<class 'bs4.element.Tag'>
print(h1['align']) #center

##################

#태그[속성="속성값"] #속성값에 공백이 없으면 속성값 사이에 " 않써도 됨 #CSS Selector
h1 = soup.select_one('h1[align=center]')
print(h1) #<h1 align="center" class="boxofficeType" id="boxofficeTypeId">일별 박스오피스</h1>
print(h1.text) #일별 박스오피스

#*= 부분 문자열 포함
h1 = soup.select_one('h1[align*=ent]')
print(h1) #<h1 align="center" class="boxofficeType" id="boxofficeTypeId">일별 박스오피스</h1>
print(h1.text) #일별 박스오피스

#속성이 id 일 경우 태그#속성값 사용 가능
h1 = soup.select_one('h1#showRangeId')
#h1 = soup.select_one('h1[id=showRangeId]')
print(h1) #<h1 class="showRange" id="showRangeId">20180220~20180220</h1>
print(h1.text) #20180220~20180220

#속성이 class 일 경우 태그.속성값 사용 가능
h1 = soup.select_one('h1.showRange')
#h1 = soup.select_one('h1[class=showRange]')
print(h1) #<h1 class="showRange" id="showRangeId">20180220~20180220</h1>
print(h1.text) #20180220~20180220

##################

#바로 상위에 center 태그가 있음
h1 = soup.select_one('center > h1')
print(h1) #<h1 class="showRange" id="showRangeId">20180220~20180220</h1>
print(h1.text) #20180220~20180220

#상위 어디엔가에 center 태그가 있음
h1 = soup.select_one('center h1')
print(h1) #<h1 class="showRange" id="showRangeId">20180220~20180220</h1>
print(h1.text) #20180220~20180220
