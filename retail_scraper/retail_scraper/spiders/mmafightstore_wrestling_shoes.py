import scrapy
import json


class MmafightstoreWrestlingShoesSpider(scrapy.Spider):
    name = "mmafightstore-wrestling-shoes"
    allowed_domains = ["mmafightstore.com.au"]
    start_urls = ["https://mmafightstore.com.au/collections/wrestling-shoes/products.json?limit=250"]

    def parse(self, response):
        data = response.json()

        yield data
    
