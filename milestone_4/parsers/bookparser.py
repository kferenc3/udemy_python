import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraper.book_parser')

class BookParser:

    def __init__(self, parent) -> None:
        logger.debug(f'New book parser created from page content.')
        self.parent = parent

    def __repr__(self) -> str:
        star = 'star' if self.rating == 1 else 'stars'
        return f'<Book {self.name}, costing {self.price} ({self.rating} {star})>'
    
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    @property
    def name(self):
        logger.debug(f'Getting the book title...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Book title is `{item_name}`')
        return item_name
    
    @property
    def href(self):
        logger.debug(f'Getting the book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        item_href = item_link.attrs['href']
        logger.debug(f'Book link is `{item_href}`')
        return item_href

    @property
    def price(self) -> float:
        logger.debug(f'Getting the book price...')
        locator = BookLocators.PRICE_LOCATOR
        price_raw = self.parent.select_one(locator).text
        regex = '^£([0-9]+\.[0-9]+$)'
        logger.debug(f'Book price (raw) is `{price_raw}`')
        return float(re.search(regex,price_raw).group(1))

    @property
    def rating(self):
        logger.debug(f'Getting the book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating[0])
        logger.debug(f'Book rating is `{rating_number}`')
        return rating_number