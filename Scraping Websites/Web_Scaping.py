# Learning how to web scrape using Chat GPT as a reference
# Library used is BeautifulSoup
# The program can scrape a select website for links then puts all those links into a csv file

import requests 
from bs4 import BeautifulSoup
import csv

url = 'https://www.reddit.com' #Choose the website you would like to scrape for links. Check Terms of Service before scraping.
response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, 'html.parser')

links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))

with open('links.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link'])
    for link in links:
        writer.writerow([link])

