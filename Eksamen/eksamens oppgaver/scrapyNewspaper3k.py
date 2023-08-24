import urllib.request
import re
from urllib.parse import urljoin
import csv
from newspaper import Article
import spacy
import nltk
from collections import Counter
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")
url = "https://simple.wikipedia.org/wiki/The_Hobbit"
response = urllib.request.urlopen(url)
html = response.read()

bs = BeautifulSoup(html, "html.parser")

#collecting text from all paragraphs into one string.
doc = ""
for p in bs.find_all("p"):
    doc += p.text
doc = nlp(doc)

#TASK1  print all tokens from the string
def find_tokens():
    for token in doc:
        print(token.text)
find_tokens()

#TASK2 find nouns
def find_nouns():
    for token in doc:
        if token.pos_ == "NOUN":
            print(token)
find_nouns()

#TASK3  find enteties
def find_enteties():
    for ent in doc.ents:
        print(ent.text)
find_enteties()

#TASK4  print the 10 most mentioned enteties
def most_mentioned_enteties():
    unique_ents = []
    for ent in doc.ents:
            unique_ents.append(ent.text)
    frequencies = Counter([ent.text for ent in doc.ents])
    print(frequencies.most_common(10))

most_mentioned_enteties()





