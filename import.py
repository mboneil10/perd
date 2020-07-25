from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
# TODO: fill in page
page = "https://www.mass.gov/service-details/missing-persons"
person = []
index = 0

driver.get(page)

# start with one person and all their attrs.
content = driver.page_source
data = BeautifulSoup(content, features = "html.parser")

person_table = data.findAll('tr', attrs={})
for row in person_table:
    keys = row.findAll('td', attrs={})
    value = (keys[1]).text.strip()
    person.append(value)

driver.close()

df = pd.DataFrame({'Heading':person})
df.to_csv('products.csv', index=False, encoding='utf-8')