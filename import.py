from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

# Functions
def data_import():
    titles = []
    i = 20
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = "https://www.stitcher.com/podcast/crime-in-sports/small-town-murder"
    driver.get(page)
    while i > 0:
        driver.find_element_by_class_name('loadMore').click()
        i = i - 1
    content = driver.page_source
    data = BeautifulSoup(content, features="html.parser")
    for episode in data.findAll('div', attrs={'id': 'episodeContainer'}):
        title = episode.find('a', attrs={'class': 'title'}).text.strip()
        titles.append(title)
    driver.close()
    return titles

# TODO: Remove titles starting with "Bonus", ending in "- Part: 2", "- Part:1"
# TODO: Incorporate more titles and the towns
def location(list):
    locations = []
    index = 0
    for title in list:
    # find LAST "in" in the title (as a full word)
        split_title = re.search('(?<=in)( \w+)*', title)
        index_of_location = split_title.start(0)
        location = title[index_of_location:].strip()
        locations.append(location)
        time.sleep(5)
    return locations

def ranking(list):
    loc_count = {}
    for loc in list:
        if loc in loc_count:
            loc_count[loc] += 1
        else:
            loc_count[loc] = 1
    return loc_count

# Program
print(data_import())
# print(ranking(location(data_import())))
# df = pd.DataFrame({'Titles': data_import()})
# df.to_csv('titles.csv', index=False, encoding='utf-8')
