# 아티스트(예술가) 찾기 (웹 브라우저 제어)

# National Gallery of Art
# Site :  https://www.nga.gov/collection/artists.html

# Selenium: 웹 어플리케이션을 위한 테스팅 프레임워크 (BeautifulSoup의 한계 해결)
from selenium import webdriver
import time
from bs4 import BeautifulSoup

path = "D:/develop/download/Library/python_webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)
url = 'https://www.nga.gov/collection/artists.html'
driver.get(url)
time.sleep(3)
text = driver.page_source
# print(text)
soup = BeautifulSoup(text, 'html.parser')

for li in soup.select('#returns > li'):
    title = ''
    lifespan = ''
    description = ''
    if li.dl.select_one('dt[class="title"]'):
        title = li.dl.select_one('dt[class="title"]').text  # ***Error***
    if li.dl.select_one('dd[class="lifespan"]'):
        lifespan = li.dl.select_one('dd[class="lifespan"]').text
    if li.dl.select_one('dd[class="description"]'):
        description = li.dl.select_one('dd[class="description"]').text
    print(title, lifespan, description)

driver.quit()

'''
"Greek A" Factory Dutch, active 1658 - 1722 Grieksche A Factory
107 Workshop  Shirreff, Jack
2 Bit Comics American 
7 Freds Press American, active 1970s 
A. B.  
A. Lublin  
Aachen, Hans von German, 1552 - 1615 Achen, Johann von, Aken, Johann von
Aarland, Johann Carl Wilhelm German, 1822 - 1906 
Abakanowicz, Magdalena Polish, 1930 - 2017 Abakanowicz, Marta
Abate, Niccolò dell' Italian, 1509 or 1512 - 1571 Abbate, Niccol&ograve; dell'
Abbati, Pietro Giovanni Italian, active 1700/1710 
Abbatini, Guido Ubaldo Italian, c. 1600 - 1656 
Abbe, Elfriede Martha American, born 1919 
Abbé, Salomon van British, 1883 - 1955 
Abbe, William Parker American, 1916 - 1983 
Abbey, Edwin Austin American, 1852 - 1911 
Abbiati, Giuseppe Italian, active 1730s 
Abbot, John American, 1751 - 1839 
Abbott, Berenice American, 1898 - 1991 
Abbott, John White British, 1763 - 1851 
'''
