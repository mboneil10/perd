from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

page = "https://podbay.fm/podcast/1194755213"

episodes = []
titles = []
descriptions = []

driver.get(page)

# TODO: start with the title
content = driver.page_source
data = BeautifulSoup(content, features = "html.parser")

for episode in data.findAll('div', attrs={'class':'preview'}):
    title = episode.find('div', attrs={'class':'episode-title'}).text.strip()
    titles.append(title)

driver.close()

df = pd.DataFrame({'Titles':titles})
df.to_csv('products.csv', index=False, encoding='utf-8')