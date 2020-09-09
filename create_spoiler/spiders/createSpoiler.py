import scrapy
from wordpressApi import checkAndPost
from time import sleep

class CreatespoilerSpider(scrapy.Spider):
    name = 'createSpoiler'
    allowed_domains = ['mangafast.net']
    start_urls = ['https://mangafast.net/create-spoiler/']

    def parse(self, response):
        kontens = response.xpath('//li')
        for konten in kontens:
            sleep(2)
            judul = konten.xpath('./h1/text()').extract_first()
            judul - str(judul) + ' Spoiler'
            slug = konten.xpath('./h2/text()').extract_first()
            slug = str(slug) + '-spoiler'
            tags = konten.xpath('./span').extract()
            tags = ','.join(tags)

            lastChapter = konten.xpath('./h3/text()').extract_first()

            data = {
                'title' : judul,
                'tags' : tags,
                'chapter' : lastChapter
            }
            
            yield checkAndPost(slugString=slug, stringTypePost='posts', data= data)

