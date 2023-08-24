from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
visited_pages = 0


driver = webdriver.Chrome()

# start url
driver.get("https://twitter.com/search?q=%23SpaceX")

time.sleep(5)

# venter til siden har lastet
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="react-root"]')))

#Kjører en while loop som finner linker via # og åpner den nye siden.
while visited_pages < 6:
    wait = WebDriverWait(driver, 20)
    # finner alle "#"linker
    elements = driver.find_elements(By.XPATH, "//a[@dir = 'ltr'][contains(@href, 'hashtag')]")
    hrefs = []
    for elem in elements:
        hrefs.append(elem.get_attribute("href"))
    # velger en tilfeldig link
    random_hashtag = random.choice(hrefs)

    # åpner linken
    driver.get(random_hashtag)
    time.sleep(5)
    # venter på at siden laster
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="react-root"]')))

    # teller besøkte sider.
    visited_pages += 1

# Close the browser session
driver.quit()
