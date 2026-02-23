from datetime import date
import scrapy
import json


class PaceAthleticSpider(scrapy.Spider):
    name = "pace-athletic"
    allowed_domains = ["www.paceathletic.com"]
    start_urls = ["https://www.paceathletic.com/collections/mens-running-shoes/products.json?limit=250"]
    page_no = 1 


    def parse(self, response):
        data = response.json()
        
        if data['products'] != []:
            product_list_raw = data['products']
            product_list_clean = []
            for product in product_list_raw:
                for variant in product['variants']:
                    product_list_clean.append({
                        "id": variant['id'],
                        "title": product['title'],
                        "created_at": product['created_at'],
                        "updated_at": product['updated_at'],
                        "vendor": product['vendor'],
                        "product_type": product['product_type'],
                        "price": variant['price'],
                        "size": variant['option2'],
                        "colour": variant['option1'],
                        "availability": variant['available'],
                        "link": f"https://www.paceathletic.com/products/{product['handle']}?variant={variant['id']}",
                        "scraped_at": str(date.today()) 
                    })
            yield { "products": product_list_clean }
            self.page_no += 1
            yield response.follow(f"https://www.paceathletic.com/collections/mens-running-shoes/products.json?limit=250&page={self.page_no}", callback=self.parse)
