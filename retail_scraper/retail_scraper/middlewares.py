from scrapy.exceptions import CloseSpider

class Stop406Middleware:
    def process_response(self, request, response, spider):
        if response.status == 406:
            spider.crawler.engine.close_spider(spider, 'Recieved 406 HTTP Error. Stopping spider...')
            raise CloseSpider('Recieved 406 HTTP Error. Stopping spider...')
            raise IgnoreRequest()
        return response

