from scrapy.spiders import CrawlSpider, Rule
from scrapingoblig.items import Scrapingoblig_
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin

#min crawler
class Vergespider(CrawlSpider):
    name = "my_crawler"
    allowed_domains = ["theverge.com"]
    start_urls = ['https://www.theverge.com/reviews']

    # regler for uthenting av linker. første for å finne linkene jeg ser etter. Regel nummer to for å utelukke andre linker
    rules = [Rule(LinkExtractor(allow=(r'https://www\.theverge\.com/\d+/\S+',)), callback='parse_items', follow=True, cb_kwargs={'is_article':True}),
             Rule(LinkExtractor(allow=r'.*'), callback='parse_items', cb_kwargs={'is_article':False})]

#funksjon som henter ut selve informasjonen
    def parse_items(self, response, is_article):
        base_url = "https//:www.theverge.com"

        if is_article:
            the_verge = Scrapingoblig_()
            the_verge['url'] = response.url
            the_verge['title'] = response.xpath('//h1/text()').extract_first()
            the_verge['authorname'] = response.xpath('//a[contains(@href,"author")]/text()').get()
            the_verge['author_profile'] = base_url + response.xpath('//a[contains(@href,"author")]/@href').get()
            yield the_verge
        else:
            pass
