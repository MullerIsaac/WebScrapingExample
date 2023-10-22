import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"

    start_urls = ["https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-2&page={i}" for i in range(1, 20)]

    def parse(self, response, **kwargs):
        
        for i in response.xpath('//li[@class="promotion-item avg"]'):
            price = i.xpath('.//span[@class="andes-money-amount__fraction"]//text()').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]//text()').get()
            link = i.xpath('.//a/@href').get()

            yield{
                'price' : price,
                'title' : title, 
                'link' : link
            }
