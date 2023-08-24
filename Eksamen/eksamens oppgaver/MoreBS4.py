import urllib.request
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import random
import re

url = "https://simple.wikipedia.org/wiki/Abbey_Road"
response = urllib.request.urlopen(url)
html = response.read()
bs = BeautifulSoup(html, "html.parser")

#TASK1 find all hrefs attributes found in a tags.
def task1():
    try:
        links = bs.find_all("a")
        for link in links:
            link = link.get("href")
            print(link)
    except IndexError as e:
        pass
#task1()

#TASK2 make a function that only find internal links(/wiki/)
def task2():
    base_url = "https://simple.wikipedia.org"
    try:
        links = bs.find_all("a")
        for link in links:
            link = link.get("href")
            if link.startswith("/wiki"):
                print(link)
    except IndexError as e:
        pass
#task2()


#TASK3     #make the relative links from task 2 into absolute links
def task3():
    base_url = "https://simple.wikipedia.org"
    try:
        links = bs.find_all("a")
        for link in links:
            link = link.get("href")
            if link is not None and link.startswith("/wiki/"):
                full_link = urljoin(base_url, link)
                print(full_link)
            else:
                continue
    except IndexError as e:
        pass
#task3()


#TASK4 write a function that selects 10 random absolute links from task 3. and visit them print visited links and heading of the link

def task4():
    base_url = "https://simple.wikipedia.org"
    absolute_links = []
    try:
        links = bs.find_all("a")
        for link in links:
            link = link.get("href")
            if link is not None and link.startswith("/wiki/"):
                full_link = urljoin(base_url, link)
                absolute_links.append(full_link)
            else:
                continue
    except IndexError as e:
        pass

    counter = 0
    while counter <= 10:
        random_links_visit = random.sample(absolute_links, 10)
        for random_link in random_links_visit:
            if counter > 9:
                break
            else:
                counter +=1
                print(random_link)
                new_response = urllib.request.urlopen(random_link)
                soup = BeautifulSoup(new_response, "html.parser")
                header = soup.find("h1").text
                print(header)
                print(counter)
#task4()

#TASK 5     function for crawling all albums and printing album duration and release year.
def task5():
    url = "https://simple.wikipedia.org/wiki/Category:The_Beatles_albums"
    base_url = "https://simple.wikipedia.org"
    response = urllib.request.urlopen(url)
    html = response.read()

    bsoup = BeautifulSoup(html, "html.parser")
    albums_location = bsoup.find("div", attrs={"class":"mw-category-generated"})
    links = albums_location.find_all("a")

    album_list = []
    for link in links:
        link = link.get("href")
        link = urljoin(base_url, link)
        album_list.append(link)

    for album in album_list:
        while len(album_list) == 0:
            break
        else:
            new_response = urllib.request.urlopen(album)
            html_new = response.read
            b_s = BeautifulSoup(html_new, "html.parser")

            release_date = b_s.find("td", attrs={"class":"infobox-data category"})
            print(release_date)

task5()
