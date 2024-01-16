from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Inspect the elements that needs to be scrapped. Here, we want the quotes and the authors.
# The quotes are spans with class='text' and authors are small with class='author'

quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

# for quote in quotes:
#     print(quote.text)
# for author in authors:
#     print(author.text)

for quote, author in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)


# We can save this data in csv files

file = open("scraped_BfSoup_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    writer.writerow([quote.text, author.text])
file.close()