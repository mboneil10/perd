from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

page = "https://podcasts.apple.com/us/podcast/small-town-murder/id1194755213"

title = []
description = []

driver.get(page)

# TODO: start with one episode and record attrs.
content = driver.page_source
data = BeautifulSoup(content, features = "html.parser")

for row in data.findAll('tr', attrs={}):
    keys = row.findAll('td', attrs={})
    value = (keys[1]).text.strip()
    person.append(value)

driver.close()

df = pd.DataFrame({'Heading':person})
df.to_csv('products.csv', index=False, encoding='utf-8')