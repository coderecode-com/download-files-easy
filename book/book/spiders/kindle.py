import scrapy


class KindleSpider(scrapy.Spider):
    name = 'kindle'
    start_urls = ['https://www.gutenberg.org/ebooks/bookshelf/68']

    def parse(self, response):
        for book in response.css('.booklink > a ::attr(href)').getall():
            book = response.urljoin(book)
            yield scrapy.Request(book, callback=self.book_details)
    
    def book_details(self, response):
        
