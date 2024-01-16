from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

# Look at the table and it's tag and class name used to define it by inspecting the element
# If there are more tables with same class names, we are using find library which gives the details of the
# first occurring table by default. If this is not required, we can do findall and index to whichever table
# is desired.

# <table class="wikitable sortable jquery-tablesorter">
# <caption>

soup.find('table')  # This gives the first table details

soup.find_all('table')  # This gives data of all tables available in the website

soup.find_all('table')[1]  # This is the info that we want

# We can also get this info specifying the class name that is used to define this table

soup.find('table', class_='wikitable sortable')

table = soup.find_all('table')[1]
# print(table)

# We can get all the titles by finding all the table headers in th tags
# world_titles = soup.find_all('th') # This pulls in ALL the headers

world_titles = table.find_all('th')
# print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)

df = pd.DataFrame(columns=world_table_titles)
# print(df)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data

# print(df)
#df.to_csv(r'/Users/sindhus/Documents/Projects/Scrapper/Scraping with pandas/scraped_pandas_data.csv', index=False)
