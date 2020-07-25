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

# TODO: start with one person and record their attrs.
# click on the person's link here
content = driver.page_source
data = BeautifulSoup(content, features = "html.parser")

for row in data.findAll('tr', attrs={}):
    keys = row.findAll('td', attrs={})
    value = (keys[1]).text.strip()
    person.append(value)

driver.close()

df = pd.DataFrame({'Heading':person})
df.to_csv('products.csv', index=False, encoding='utf-8')