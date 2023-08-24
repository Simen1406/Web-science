from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
start_url = "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index"
driver.get(start_url)
time.sleep(3)

locate_webpage = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//table[1]')))

find_table = driver.find_elements(By.XPATH, '//table[@class = "wikitable sortable plainrowheaders jquery-tablesorter"]')
for elem in find_table[1]:
    print(elem)


