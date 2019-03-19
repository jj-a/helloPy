# 아티스트(예술가) 찾기 (웹 브라우저 네트워크 메뉴)

# National Gallery of Art
# Site :  https://www.nga.gov/collection/artists.html

import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'https://www.nga.gov/collection/artists/jcr:content/parmain/facetcomponent/parList/artistlistings.pageSize__20.pageNumber__1.json?_=1524568113289'
res = requests.get(url, headers=headers)
text = res.text
# print(text)
d = json.loads(text)

for record in d['artists']:
    print(record['name'], record['url'], record['nationality'])

'''
&quot;Greek A&quot; Factory /content/ngaweb/collection/artist-info.41979.html Dutch
107 Workshop /content/ngaweb/collection/artist-info.49297.html None
2 Bit Comics /content/ngaweb/collection/artist-info.47008.html American
7 Freds Press /content/ngaweb/collection/artist-info.48225.html American
A. B. /content/ngaweb/collection/artist-info.17840.html None
A. Lublin /content/ngaweb/collection/artist-info.49107.html American
Aachen, Hans von /content/ngaweb/collection/artist-info.5566.html German
Aarland, Johann Carl Wilhelm /content/ngaweb/collection/artist-info.48785.html German
Abakanowicz, Magdalena /content/ngaweb/collection/artist-info.10278.html Polish
Abate, Niccol&ograve; dell' /content/ngaweb/collection/artist-info.3474.html Italian
Abbati, Pietro Giovanni /content/ngaweb/collection/artist-info.21155.html Italian
Abbatini, Guido Ubaldo /content/ngaweb/collection/artist-info.19745.html Italian
Abbe, Elfriede Martha /content/ngaweb/collection/artist-info.2855.html American
Abb&eacute;, Salomon van /content/ngaweb/collection/artist-info.2856.html British
Abbe, William Parker /content/ngaweb/collection/artist-info.33127.html American
Abbey, Edwin Austin /content/ngaweb/collection/artist-info.2337.html American
Abbiati, Giuseppe /content/ngaweb/collection/artist-info.14725.html Italian
Abbot, John /content/ngaweb/collection/artist-info.40407.html American
Abbott, Berenice /content/ngaweb/collection/artist-info.13553.html American
Abbott, John White /content/ngaweb/collection/artist-info.10979.html British
'''
