import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import random

# Open the URL
url = "https://simple.wikipedia.org/wiki/Abbey_Road"
response = urllib.request.urlopen(url)

# Read the HTML content of the page
html = response.read()

# Parse the HTML content of the page
soup = BeautifulSoup(html, "html.parser")



# Seminar 4:

# Task 1 (Make a function that prints all links (a) tags) on the webpage.
# Since you might get a KeyError you should write an exception handling for this.

def all_links():
    links = soup.find('div', attrs={"id": "bodyContent"}).find_all("a")
    for a in links:
        try:
            print(a["href"])
        except KeyError as e:
            print("KeyError")

# Task 2: From Task 1 you might notice that many links starts with "/wiki/....". These
# are internal wikipedia links that point to other wikipedia articles or resources.
# Make a function that only finds the links that start with /wiki/.

def all_wiki_links():
    links = soup.find('div', attrs={"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    for a in links:
        try:
            print(a["href"])
        except KeyError as e:
            print("KeyError")


# Task 3: The links from task 2 are only relative URL's and can therefore not be visited right now.
# Improve the function from task 2 by using the "urljoin" library to "join" the domain "https://en.wikipedia.org" with each of the links.
# Make the function return a list of all the absolute urls it found.


def absolute_links():
    link_list = []
    domain_url = "https://en.wikipedia.org"
    links = soup.find('div', attrs={"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    for a in links:
        try:
            absolute_url = urljoin(domain_url, a["href"])
            #print(absolute_url)
            link_list.append(absolute_url)
        except KeyError as e:
            print("KeyError")

    return link_list


# Task 4 - Write a function that picks 10 random links (from task 3) and visits them with urlopen. Print the links
# you are visiting as well as the h1 header on those pages.


def visit_10_random_links():
    links = absolute_links()
    links_todo = []
    i = 0
    while i < 10:
        links_todo.append(links[random.randrange(0,len(links))])
        i+=1

    links_visited = set()

    while links_todo:
        visit_link = links_todo.pop()
        if visit_link not in links_visited:
            links_visited.add(visit_link)
            print("Now visiting: ", visit_link)
            html = urllib.request.urlopen(visit_link).read()
            soup = BeautifulSoup(html, "html.parser")
            print("Header is: ", soup.find("h1").text)


# Task 5 : Make a function that crawls all albums that you can find on this wikipage: "https://simple.wikipedia.org/wiki/Category:The_Beatles_albums .
# Make the crawler print the release date and duration of all the albums.
# Notice that all the album pages have the same info-table on the right side, where we can find this information.

def crawl_albums():
    domain = "https://en.wikipedia.org"

    url = "https://simple.wikipedia.org/wiki/Category:The_Beatles_albums"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    albums = soup.find('div', attrs={"class": "mw-category mw-category-columns"}).find_all("li")

    links_todo = []
    links_visited = set()

    for album in albums:
        try:
            link = album.find("a")["href"]
            absolute_url = urljoin(domain, link)
            links_todo.append(absolute_url)
        except KeyError as e:
            pass

    while links_todo:
        visit_link = links_todo.pop()
        if visit_link not in links_visited:
            links_visited.add(visit_link)
            html = urllib.request.urlopen(visit_link).read()
            soup = BeautifulSoup(html, "html.parser")
            try:
                print("Now visiting: ", visit_link, "\n")
                release_date = soup.find("td", attrs={"class":"infobox-data published"}).text
                duration = soup.find("span", attrs={"class":"duration"}).text
                genres = soup.find("td", attrs={"class":"infobox-data category hlist"}).text
                print("Information crawled from album: ", soup.find("h1").text)
                print("Release Date: ", release_date)
                print("Duration: ", duration)
                print("Genres: ", genres, "\n\n")
            except AttributeError as e:
                pass


if __name__ == '__main__':
    # Seminar 4 - Web Crawling
    #all_links():
    #all_wiki_links():
    #absolute_links()
    #visit_10_random_links()
    crawl_albums()
