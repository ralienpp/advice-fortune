import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from advice.items import AdviceItem


class AdviceSpider(CrawlSpider):
    name = 'advice'
    allowed_domains = ['fucking-great-advice.ru']
    start_urls = ['http://fucking-great-advice.ru/advice/1/']

    url_regex = '^http:\/\/fucking-great-advice.ru\/advice\/\d+\/+'

    rules = (
        # Extract links matching 'advice/' and parse them with the spider's method parse
        Rule(LinkExtractor(allow=(url_regex, ), unique=True), callback='get_advice', follow=True),
    )

    # this interferes with the LinkExtractor, which has its own parse method to get things done
    # if I use this function, then I lose the LinkExtractor's default behaviour, which is good
    # for this specific site
    # def parse(self, response):
    #     for url in response.xpath("//ul[@id='tags']/li/a/@href").extract():
    #         yield scrapy.Request(url, callback=self.get_advice)


    def get_advice(self, response):
        item = AdviceItem()
        # import pdb; pdb.set_trace()
        # the number is in the URL 'http://fucking-great-advice.ru/advice/1/'
        item['number'] = int(response.url.split('/')[-2])

        try:  
            item['advice'] = response.xpath("//p[@id='advice']/text()").extract()[0]
        except:
            #import pdb; pdb.set_trace()
            print('Skipping %s' % item['number'])
        else:
            print(item['advice'])
            yield item


#TODO consider crawling via google cache
