import re
import logging

from locators.books_locators import BookLocator

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, page):
        # print('*****************************')
        self.page = page

    def __repr__(self):
        # print('!!!!!!!!!!!!!@@@@@@@@@@@@@@@')
        return f'{self.name}'

         
    @property
    def name(self):
        locator=BookLocator.NAME_LOCATOR
        item_link=self.page.select_one(locator)
        item_name=item_link.attrs['title']
        return item_name
           
    @property 
    def link(self):
        locator=BookLocator.LINK_LOCATOR
        item_link=self.page.select_one(locator).attrs['href']
        return item_link
           
    @property 
    def price(self):
        locator=BookLocator.PRICE_LOCATOR
        item_price=self.page.select_one(locator).string
        pattern='£([0-9]+\.[0-9]+)'
        matcher=re.search(pattern,item_price)
        temp=matcher.group(1)
        return float(temp)
           
    @property 
    def rating(self):
        locator=BookLocator.RATING_LOCATOR
        ratingTag=self.page.select_one(locator)
        classes=ratingTag.attrs['class']
        rating_class=[r for r in classes if r!='star-rating']
        rating_num=BookParser.RATINGS.get(rating_class[0])
        return  rating_num