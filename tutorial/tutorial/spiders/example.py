import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://www.ece.utexas.edu/people/faculty/mary-eberlein']

    def parse(self, response):
        print(response.xpath('//span[@class="field-content"]/text()').get())

