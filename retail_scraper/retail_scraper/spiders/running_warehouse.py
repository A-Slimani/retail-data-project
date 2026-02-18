from datetime import date
import scrapy
import json
import re


class RunningWarehouseSpider(scrapy.Spider):
    name = "running-warehouse"
    allowed_domains = ["www.runningwarehouse.com.au"]
    start_urls = [
        "https://www.runningwarehouse.com.au/_Mens_Neutral_Running_Shoes/catpage-RWMFNEUT.html",
        "https://www.runningwarehouse.com.au/Mens_Road_Running_Shoes/catpage-MRDSH.html", 
        "https://www.runningwarehouse.com.au/Mens_Stability_Running_Shoes/catpage-MFSTAB.html"
    ]


    def parse(self, response):
        shoe_list = response.xpath("//a[@class='cattable-wrap-cell-info']/@href").getall()
        for shoe in shoe_list:
            yield(response.follow(shoe, self.parse_shoe))


    def parse_shoe(self, response):
        model_number = re.sub(r'\n', '', response.xpath("//p[@class='mb-3']/text()").get()).strip()
        name = response.xpath("//h1[contains(@class, 'desc_top-head-title')]/text()").get()
        colour = response.xpath("//div[@class='desc_top-head-style']/text()").get().split('-')[-1].strip()
        price = response.xpath("//span[@class='afterpay-full_price']/mark/text()").get()
        scraped_at = str(date.today()) 
        sizes_raw = response.xpath("//table[contains(@class, 'styled_subproduct_list')]/@data-json_style_sort").get()
        link = response.url 
        
        if sizes_raw:
            sizes_raw_json = json.loads(sizes_raw)
        else:
            return

        yield {
           "model_number": model_number,
           "name": name,
           "link": link,
           "colour": colour,
           "price": price,
           "sizes_raw_json": sizes_raw_json,
           "scraped_at": scraped_at
         }
