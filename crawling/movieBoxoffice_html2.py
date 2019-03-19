# 영화 일별 박스오피스 수집 - html 파서 2

# 하위 태그객체 접근
# : 태그객체 = 태그객체.태그객체
# 태그객체 = 태그객체.select_one(CSS Selector)
# 리스트 = 태그객체.select(CSS Selector)

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

table = soup.select_one('table')
print(table)
'''
<table align="center" border="1">
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
'''
print(table.text)
'''
순위 (rank)
신규진입여부 (rankOldAndNew)
영화코드 (movieCd)
영화명 (movieNm)
매출액 (salesAmt)
관객수 (audiCnt)


1
OLD
20170561
블랙 팬서
1339822000
171158
'''

print(table.tr)
'''
<tr>
<td class="rank">순위 (rank)</td>
<td class="rankOldAndNew">신규진입여부 (rankOldAndNew)</td>
<td class="movieCd">영화코드 (movieCd)</td>
<td class="movieNm">영화명 (movieNm)</td>
<td class="salesAmt">매출액 (salesAmt)</td>
<td class="audiCnt">관객수 (audiCnt)</td>
</tr>
'''
#print(table.select_one('tr'))
print(table.tr.text)
'''
순위 (rank)
신규진입여부 (rankOldAndNew)
영화코드 (movieCd)
영화명 (movieNm)
매출액 (salesAmt)
관객수 (audiCnt)
'''

print(table.tr.td) #<td class="rank">순위 (rank)</td>
print(table.tr.td.text) #순위 (rank)
