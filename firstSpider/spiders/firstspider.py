import scrapy
from scrapy.selector import  Selector
from firstSpider.items import HouseItem

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
            # yield{
            #     'title': house.xpath('dl/dd[contains(@class,"title")]/a/text()').extract()[0],
            #     'house_tpye':  house.xpath('dl/dd[contains(@class,"size")]/@data-huxing').extract()[0],
            #     'size':  house.xpath('dl/dd[contains(@class,"size")]/@data-area').extract()[0],
            #     'rent_style':  house.xpath('dl/dd[contains(@class,"size")]/span[contains(@class,"js-huxing")]/text()').extract()[0],
            #     'area': house.xpath('dl/dd[contains(@class,"address")]/span/a[@class="address-eara"]/text()').extract(),
            #     'feature': house.xpath('dl/dd[contains(@class,"feature")]/span/text()').re_first(r'[1-3]号线'),
            #     'price': house.xpath('dl/dd/div[@class="price"]/span[@class="num"]/text()').extract()[0]
            # }
            houseItem =  HouseItem()
            houseItem['title'] =  house.xpath('dl/dd[contains(@class,"title")]/a/text()').extract()[0]
            houseItem['house_type'] = house.xpath('dl/dd[contains(@class,"size")]/@data-huxing').extract()[0]
            houseItem['size'] = house.xpath('dl/dd[contains(@class,"size")]/@data-area').extract()[0]
            houseItem['rent_style'] = house.xpath('dl/dd[contains(@class,"size")]/span[contains(@class,"js-huxing")]/text()').extract()[0]
            houseItem['area'] = house.xpath('dl/dd[contains(@class,"address")]/span/a[@class="address-eara"]/text()').extract()
            houseItem['feature'] = house.xpath('dl/dd[contains(@class,"feature")]/span/text()').re_first(r'[1-3]号线')
            houseItem['price'] = house.xpath('dl/dd/div[@class="price"]/span[@class="num"]/text()').extract()[0]
            yield  houseItem
        # next_page = response.selector.xpath('//div[@class="pageBox"]/ul/li/a[@class="next"]/@href').extract()[0]
        # print(next_page)
        # base_url = "http://xa.ganji.com"
        # if next_page is not None:
        #     nextUrl = base_url + next_page
        #     print(nextUrl)
        #     yield scrapy.Request(nextUrl,callback=self.parse)



