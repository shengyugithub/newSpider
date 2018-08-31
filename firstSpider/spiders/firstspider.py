import scrapy
from scrapy.selector import  Selector

class firstSpider(scrapy.Spider):
    name = "first"
    start_urls = ['http://xa.ganji.com/fang1/',]

    # custom_settings = {
    #     'referer': 'https://cdata.58.com/nfp.html?from=weba_fzq&clientType=1&callback=xzfzcallback&token=YE8Bx9I2Mp5SEzGjr0TtEAu1n4%2BPQT46j4vzsphmS3WVK%2F4eOVcO9G6dXZXtSENgin35brBb%2F%2FeSODvMgkQULA%3D%3D',
    #     'cookie': 'id58=CwzxCFuEsW6rSMSr9UxWng==; xzuid=0c2634fe-8177-42bc-86d8-15145bcc1ba0',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    # }

    '''
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield  response.follow(next_page, self.parse)
    '''

    def parse(self, response):
        houses = response.selector.xpath('//div[contains(@class,"ershoufang-list")]')
        #print(houses)
        for house in houses:
            yield{
                'title': house.xpath('dl/dd[contains(@class,"title")]/a/text()').extract(),
                'price': house.xpath('dl/dd/div[@class="price"]/span[@class="num"]/text()').extract()
            }

        next_page = response.selector.xpath('//div[@class="pageBox"]/ul/li/a[@class="next"]/@href').extract()[0]
        print(next_page)
        base_url = "http://xa.ganji.com"
        if next_page is not None:
            nextUrl = base_url + next_page
            print(nextUrl)
            yield scrapy.Request(nextUrl,callback=self.parse)



