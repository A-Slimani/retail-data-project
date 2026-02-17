import scrapy


class MmafactoryWrestlingShoesSpider(scrapy.Spider):
    name = "mmafactory-wrestling-shoes"
    allowed_domains = ["mmafactory.com.au"]
    start_urls = ["https://mmafactory.com.au/footwear/wrestling-shoes"]

    def parse(self, response):
        self.logger.info(f"Status: {response.status}")
        self.logger.info(f"Status: {response.headers}")
        self.logger.info(response.xpath("//i[@class='trekky-icon-chevron-double-right']"))
