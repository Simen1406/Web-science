import urllib.request
from bs4 import BeautifulSoup
import re

# Open the URL
url = "https://simple.wikipedia.org/wiki/Abbey_Road"
response = urllib.request.urlopen(url)

# Read the HTML content of the page
html = response.read()

# Parse the HTML content of the page
soup = BeautifulSoup(html, "html.parser")

# Task 1  - Find and print the length of the album
def task1():
    print("\nTask 1: ")
    print(soup.find("span", attrs={"class": "duration"}).text, "\n")



# Task 2 - Find the genres and store them in a list
def task2():
    print("\nTask 2: ")
    genre_list = []
    for genre in soup.find("td", attrs={"class": "infobox-data category hlist"}).find_all("li"):
     print(genre.text)
     genre_list.append(genre.text)


# Task 3 - Find the genres "titles" (title attribute).
def task3():
    print("\nTask 3: ")
    genre2_list = []
    for genre in soup.find("td", attrs={"class": "infobox-data category hlist"}).find_all("a"):
     print(genre["title"])
     genre2_list.append(genre["title"])


# Task 4 - Print all song titles on side 1
def task4():
    print("\nTask 4: ")
    table = soup.find("table", attrs={"class": "tracklist"})
    for title in table.find_all("tr"):
        rows = title.find_all("td")
        # I run Exception handling here because some of the table rows
        # had inconsistent format, and there gave errors when I tried to get the song title or vocalist.
        try:
            print(rows[1].text)
        except IndexError as e:
            pass


# Task 5 # Find all links <a> (href attribute) that are nested within <p> tags.
def task5():
    print("\nTask 5: ")
    paragraphs = soup.find_all("p")
    for p in paragraphs:
     for a in p.find_all("a"):
         print(a["href"])


# Task 6 - Print all Songs with lead vocals by Mccartney
def task6():
    for table in soup.find_all("table", attrs={"class": "tracklist"}):
        for title in table.find_all("tr"):
         rows = title.find_all("td")
         # I run Exception handling here because some of the table rows
         # had inconsistent format, and there gave errors when I tried to get the song title or vocalist.

         try:
             if rows[2].text == "McCartney":
                 print(rows[1].text)
         except IndexError as e:
             pass

# PART 2 - Regex tasks
# Task 7 - Use regex with your previous code to find song titles that contains the word “you”.

links = soup.find_all("a", href=re.compile("^(?!/you/)$"))

def task7():
    for table in soup.find_all("table", attrs={"class": "tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
            try:
                # Regex search for the word "You" or "you".
                result = re.search("^.*[Yy]ou.*$", rows[1].text)
                if result != None:
                    print(result[0])
            except IndexError as e:
                pass


# Task 8 - Use regex with your previous code to find song titles that consists of exactly one word.
def task8():
    print("\nTask 8: ")
    for table in soup.find_all("table", attrs={"class": "tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
            try:
                # Regex search for only one word.
                result = re.search("^(\w+)$", rows[1].text)
                if result != None:
                    print(result[0])
            except IndexError as e:
                pass

# Task 9 - Use regex with your previous code to find songs that are 3 minutes in duration or longer.
def task9():
    print("\nTask 9: ")
    for table in soup.find_all("table", attrs={"class": "tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
            try:
                if re.search("^[3-9]:", rows[3].text) != None:
                    print(rows[1].text)
            except IndexError as e:
                pass

# Task 10  Use regex with your previous code to find the songs that have lead
# vocals by both Lennon and Mccartney, but optionally other members too.

def task10():
    print("\nTask 10: ")
    for table in soup.find_all("table", attrs={"class": "tracklist"}):
        for title in table.find_all("tr"):
            rows = title.find_all("td")
            try:
                if re.search("^(Lennon.*McCartney).*$", rows[2].text) != None:
                    print(rows[1].text)
                elif re.search("^(McCartney.*Lennon).*$", rows[2].text) != None:
                    print(rows[1].text)
            except IndexError as e:
                pass


if __name__ == '__main__':

    # Part 1 - Scraping
    #task1()
    #task2()
    #task3()
    #task4()
    #task5()
    task6()

    # Part 2 - Regex
    #task7()
    #task8()
    #task9()
    #task10()


