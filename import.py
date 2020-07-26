from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


# Functions
def data_import():
    titles = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = "https://podbay.fm/podcast/1194755213"
    driver.get(page)
    content = driver.page_source
    data = BeautifulSoup(content, features="html.parser")
    for episode in data.findAll('div', attrs={'class': 'preview'}):
        title = episode.find('div', attrs={'class': 'episode-title'}).text.strip()
        titles.append(title)
    driver.close()
    return titles

# TODO: Remove titles starting with "Bonus", ending in "- Part: 2", "- Part:1"
# TODO: Incorporate more titles and the towns
def states(list):
    states = []
    index = 0
    for title in list:
    # find LAST comma in the title
        split_title = title.split(",")
        last_index = len(split_title)-1
        state = split_title[last_index].strip()
        states.append(state)
    return states

def ranking(list):
    state_count = {}
    for state in list:
        if state in state_count:
            state_count[state] += 1
        else:
            state_count[state] = 1
    return state_count

# Program
print(ranking(states(data_import())))
# df = pd.DataFrame({'Titles': data_import()})
# df.to_csv('titles.csv', index=False, encoding='utf-8')
