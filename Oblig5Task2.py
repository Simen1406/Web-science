from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
import random
import time
import networkx as nx
import matplotlib.pyplot as plt

start = "https://twitter.com/i/flow/login"
crawl1 = "https://twitter.com/search?q=%23Bergen"
crawl2 = "https://twitter.com/search?q=%23Oslo"
driver = webdriver.Chrome()
visited_links = []



#remember to input username and password
def logging_in(driver, username, password):

    # get starting hashtag
    driver.get("https://twitter.com/i/flow/login")

    # automatic login.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text' and @type='text']")))

    login_username = driver.find_element(By.XPATH, "//input[@name='text' and @type='text']")
    login_username.send_keys(username)
    time.sleep(1)
    login_username.send_keys(Keys.RETURN)
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password' and @type='password']")))

    login_password = driver.find_element(By.XPATH, "//input[@name='password' and @type='password']")
    time.sleep(3)
    login_password.send_keys(password)
    time.sleep(1)
    login_password.send_keys(Keys.RETURN)


def visit_hashtags(driver, num_pages, crawl, graph_name):
    hashtags_found = []
    hrefs = []
    # initialize graph and visited links
    g = nx.Graph()
    global visited_links

    #logging in:
    logging_in(driver, "nemis12345", "nemispenis")
    time.sleep(5)

    #etter innlogging, så starter vi fra #oslo eller #bergen
    driver.get(crawl)
    visited_links.append(crawl)

    parsed_url = urlparse(driver.current_url)
    hashtag_node_name = parsed_url.path.split('/')[-1]
    previous_hashtag_name = hashtag_node_name

    visited_pages = 1

    while visited_pages <= num_pages:
        time.sleep(4)
        # find all hashtag links on the page
        elements = driver.find_elements(By.XPATH, "//a[@dir='ltr'][contains(@href, 'hashtag')]")

        # add current hashtag node to the graph and create an edge from the previous hashtag node.
        parsed_url = urlparse(driver.current_url)
        hashtag_node_name = parsed_url.path.split('/')[-1]
        g.add_node(hashtag_node_name)
        g.add_edge(previous_hashtag_name, hashtag_node_name)
        previous_hashtag_name = hashtag_node_name

        #find all hashtags and add them to a list for visiting.
        if elements:
            for elem in elements:
                href = elem.get_attribute("href")
                if href in visited_links:
                    continue
                else:
                    hrefs.append(href)
                    parsed_hashtag = urlparse(href)
                    hashtag = parsed_hashtag.path.split('/')[-1]

                    if hashtag not in hashtags_found:
                        hashtags_found.append(hashtag)

            for h in hashtags_found:
                g.add_node(h)
                g.add_edge(hashtag_node_name, h)
            # visit the hashtag link
            try:
                # choose a random hashtag link
                random_hashtag = random.choice(hrefs)
                driver.get(random_hashtag)
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="react-root"]')))

                # add visited link to the list of visited links
                visited_pages += 1
                visited_links.append(random_hashtag)

                #skriver grafen til et eget dokument
                nx.write_graphml(g, graph_name)
            except:
                print(f"No more pages to visit{hrefs}")
                break
        else:
            print(f"No hashtags found")
            break
    nx.draw(g, with_labels=True)
    plt.show()
    print(len(hrefs))
    print(len(visited_links))
    print(len(hashtags_found))
    return g.nodes

print(visit_hashtags(driver, 25, crawl1, "BergenHashtags.graphml"))
print(visit_hashtags(driver, 25, crawl2, "OsloHashtags.graphml"))



# må ligge til slik at det søkes for nye hashtags hver gang man besøker en ny side.


"""splitting_current_url = driver.current_url.split("?")[-1]
    url_src_value = splitting_current_url.split("=")[-1]
    hashtag_node_name = url_src_value.split("_")[0].capitalize()"""