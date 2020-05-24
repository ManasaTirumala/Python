import requests 
import re

from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocator
from parsers.book_parser import BookParser


class AllBooksPage:
    
    # page_content=requests.get("http://books.toscrape.com").content
    # test=BeautifulSoup(page_content,'html.parser').select(AllBooksPageLocator.BOOKS)[0]
    # print('***************************************************')
    # print(test)
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(BookParser(test))
    # print([BookParser(e) for e in BeautifulSoup(page_content,'html.parser').select(AllBooksPageLocator.BOOKS)[0]])
     
    def __init__(self,page_content):
        self.soup=BeautifulSoup(page_content,'html.parser')
        
    @property
    def books(self):
         return [BookParser(e) for e in self.soup.select(AllBooksPageLocator.BOOKS)]
        
    @property
    def page_num(self):
         temp=  self.soup.select_one(AllBooksPageLocator.PAGER).string
        #  print('1111111111**************')
        #  print(temp)
         pattern='Page [0-9]+ of ([0-9]+)'
         matcher=re.search(pattern , temp)
        #  print('22222222***************')
        #  print(matcher)
         pageCount=int(matcher.group(1))
        #  print('*******')
        #  print(pageCount)
         return pageCount
 
    
        