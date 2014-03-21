#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import re

page = 'https://en.wikipedia.org/wiki/List_of_Constituencies_of_the_Lok_Sabha'
tables = []
header = {'User-Agent': 'Mozilla/5.0'}

pagefetch = requests.get(page)
soup = BeautifulSoup(pagefetch.text)

table = soup.find("table", { "class" : "wikitable" })
print table
