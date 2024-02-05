import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.books.toscrape.com/')
soup = BeautifulSoup(page.content,'html.parser')

print(soup.find('h1').string)