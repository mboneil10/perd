from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

page = "https://podcasts.apple.com/us/podcast/small-town-murder/id1194755213"

episodes = []
titles = []
descriptions = []

driver.get(page)

# TODO: start with first few episodes and record attrs.
content = driver.page_source
data = BeautifulSoup(content, features = "html.parser")

for episode in data.findAll('li', attrs={'class':'ember-view tracks__track tracks__track--podcast'}):
    title = episode.find('a', attrs={'class':'link tracks__track__link--block'}).text.strip()
    titles.append(title)

driver.close()

df = pd.DataFrame({'Titles':titles})
df.to_csv('products.csv', index=False, encoding='utf-8')