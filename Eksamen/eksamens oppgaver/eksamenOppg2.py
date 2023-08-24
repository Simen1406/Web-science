from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from urllib.parse import urlsplit

driver = webdriver.Chrome()
start_url = "https://www.pythonscraping.com/pages/page3.html"
driver.get(start_url)
time.sleep(3)

wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.XPATH, "//table")))

elements = driver.find_elements(By.XPATH,'//table//img')
print(elements)
for element in elements:
    partial_link = urlsplit(element.get_attribute('src'))
    print(partial_link[2])

driver.quit()
