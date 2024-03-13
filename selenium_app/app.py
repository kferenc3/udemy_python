from selenium import webdriver
from pages.quotes_page import InvalidTagForAuthorError, QuotePage

try:
    author = input('Enter the author you would like quote\'s from: ')
    selected_tag = input("Enter your tag: ")

    chrome = webdriver.Chrome()
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotePage(chrome)

    print(page.search_for_quotes(author, selected_tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")