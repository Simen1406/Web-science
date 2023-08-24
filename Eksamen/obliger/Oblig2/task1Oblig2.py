import re
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

#task 1
html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker')
bs = BeautifulSoup(html.read(), 'html.parser')
main_url = 'http://en.wikipedia.org'
for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    full_url = urljoin(main_url, link.get('href'))
    print(full_url)



#Task 3