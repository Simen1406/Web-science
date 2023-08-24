import requests
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/web_scraping")
bs = BeautifulSoup(html, 'html.parser')

links = bs.find('div', {'class':'div-col'}).find_all('a')
for link in links:
    main_url = 'http://en.wikipedia.org'
    full_url = urljoin(main_url, link.get('href'))

    html = urlopen(full_url)
    see_also_links = BeautifulSoup(html, 'html.parser')

    if len(see_also_links.find("p").text) == 1:
        print(f" webpage: {full_url} First paragraph is:\n {see_also_links.find_all('p')[1].text}")
    else:
        print(f" webpage: {full_url} First paragraph is: \n{see_also_links.find_all('p')[0].text}")

