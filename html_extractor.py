# importing the libraries (discord.py and beautiful soup)
import requests
from bs4 import BeautifulSoup

# getting the URL of the website to extract html from
url = input("Website URL to extract data from : ")

# make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# parses the html content
soup = BeautifulSoup(html_content, "lxml")

# open, create or overwrite file for the output
file = open("extracted_html.txt", "w", encoding='utf-8')

# writes the output of prettify (clean code from the given website)
file.write(soup.prettify())
