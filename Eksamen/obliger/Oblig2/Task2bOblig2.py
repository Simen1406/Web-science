from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

#Task 2b
html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html.read(), 'html.parser')

tds = bs.find_all('td', {'class':'yes table-yes2 notheme'})
for td in tds:
    if td.parent.get_text().count('\n') > 6:
        print(td.parent.get_text())

    elif td.parent.get_text().count('\n') < 8:
        find_th = td.find_previous('th').get_text()
        find_date = td.find_previous('th').find_next_sibling('td').get_text()
        print(f"{find_th}{find_date}{td.parent.get_text()}")
