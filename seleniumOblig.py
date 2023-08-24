from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
import random
import time
import networkx as nx
import re

visited_pages = 1
visited_links = []
driver = webdriver.Chrome()
g = nx.Graph()

# start url
driver.get("https://twitter.com/login")
time.sleep(10)
driver.get("https://twitter.com/search?q=%23Bergen")
visited_links.append("https://twitter.com/search?q=%23Bergen")
g.add_node("start_node")
previous_hashtag_name = "start_node"
# venter til siden har lastet
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="react-root"]')))

#Kjører en while loop som finner linker via # og åpner den nye siden.
while visited_pages < 4:
    wait = WebDriverWait(driver, 20)
    time.sleep(4)
    # finner alle "#"linker
    elements = driver.find_elements(By.XPATH, "//a[@dir = 'ltr'][contains(@href, 'hashtag')]")

    # ligg til noden i grafen.
    parsed_url = urlparse(driver.current_url)
    hashtag_node_name = parsed_url.path.split('/')[-1]

    g.add_node(hashtag_node_name)
    g.add_edge(previous_hashtag_name, hashtag_node_name)
    # oppdaterer hashtag navn
    previous_hashtag_name = hashtag_node_name

    hrefs = []
    if elements:
        for elem in elements:
            href = elem.get_attribute("href")
            if href in visited_links:
                continue
            hrefs.append(href)


        # velger en tilfeldig link
        random_hashtag = random.choice(hrefs)

        # åpner linken
        driver.get(random_hashtag)
        time.sleep(5)
        # venter på at siden laster
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="react-root"]')))

        # teller besøkte sider og ligger linken til i besøkte sider.
        visited_pages += 1
        visited_links.append(random_hashtag)
    else:
        print(f"no hashtags found")
        break

print(visited_links)
print(g.nodes)
# Close the browser session
driver.quit()
