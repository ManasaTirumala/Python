import requests 
from pages.all_books_page import AllBooksPage


page_content=requests.get("http://books.toscrape.com").content
page=AllBooksPage(page_content)
books=page.books

# for pages 1-50 if we want to get all teh books
for page_num in range(1,page.page_num):
    url=f'http://books.toscrape.com/catalog/page-{page_num+1}.html'
    page_content=requests.get(url).content
    page=AllBooksPage(page_content)
    books.extend(page.books)

@property
def scrape_url(self):
        self.scrape_url=page_content
        return self.scrape_url