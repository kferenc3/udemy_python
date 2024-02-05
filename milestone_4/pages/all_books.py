import re
import logging
from bs4 import BeautifulSoup
from locators.all_books_page import AllBookPageLocators
from parsers.bookparser import BookParser

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content) -> None:
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')
    
    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBookPageLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(AllBookPageLocators.BOOKS)]
    
    @property
    def page_count(self):
        logger.debug('Finding all number of catalog pages available...')
        content = self.soup.select_one(AllBookPageLocators.PAGES).string
        pages = int(re.search('Page [0-9]+ of ([0-9]+)', content).group(1)) 
        logger.debug(f'Extraced number of pages as integer: `{pages}`')
        return pages