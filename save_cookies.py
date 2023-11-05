import pickle
import time
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()

option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
option.binary_location = '/usr/bin/chromium-browser'

driver = webdriver.Chrome(options=option)

driver.get('https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=27434&SortBy=LastSeen&Order=desc')

time.sleep(60)

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.quit()
