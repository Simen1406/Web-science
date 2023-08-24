import urllib.request
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

# Open the URL
url = "https://simple.wikipedia.org/wiki/Abbey_Road"
response = urllib.request.urlopen(url)
html = response.read()

bs = BeautifulSoup(html, "html.parser")

#TASK1
album_tables = bs.find("span", attrs={"class":"duration"}).text
print(album_tables)

#TASK4
#find and print titles of songs from the first page of the album:
titles_list = []
table = bs.find("table", attrs={"class":"tracklist"})
titles = table.find_all("a")
for title in titles:
    titles_list.append(title.get_text())
print(titles_list)

#TASK5
#find all a tags within paragraphs(p) use try, except.
base_url = url
paragraphs = bs.find_all("p")
hrefs = []
for p in paragraphs:
    try:
        links = p.find_all("a")
        for link in links:
            href = link.get("href")
            full_href = urljoin(base_url, href)
            hrefs.append(full_href)
    except AttributeError:
        print("no hrefs")
print(hrefs)


#TASK6
# Task 6 - Print all Songs with lead vocals by Mccartney
def task6():
    songs_Mcartney = []
    print("\nTask 6: ")
    for table in bs.find_all("table", attrs={"class":"tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
 # I run Exception handling here because some of the table rows
 # had inconsistent format, and there gave errors when I tried to get the song title or vocalist.
        try:
            if rows[2].text == "McCartney":
                songs_Mcartney.append(rows[1].text)
                print(songs_Mcartney)
        except IndexError as e:
             pass

task6()

#TASK7
#REGEX
links = bs.find_all("a", href=re.compile("^(?!/you/)$"))
def task7():
    print("\nTask 7: ")
    for table in bs.find_all("table", attrs={"class":"tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
            try:
 # Regex search for the word "You" or "you".
                result = re.search("^.*[Yy]ou.*$", rows[1].text)
                if result != None:
                    print(result[0])
            except IndexError as e:
                pass

task7()
