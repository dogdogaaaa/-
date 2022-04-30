import scrapy
from scrapy import Request
from ..items import PoemscrapyItem


class PoemspiderSpider(scrapy.Spider):
    name = 'poemSpider'
    allowed_domains = ['gushiwen.cn']
    start_urls = ['http://so.gushiwen.cn/mingjus/']

    def parse(self, response):
        for box in response.xpath('//*[@id="html"]/body/div[2]/div[1]/div[2]/div'):
            # 获取每句名句的链接
            url = 'https://so.gushiwen.cn' + box.xpath('.//@href').get()
            # 获取每句名句内容
            sentence = box.xpath('.//a[1]/text()').get()
            source = box.xpath('.//a[2]/text()').get()
            # 实例化容器
            item = PoemscrapyItem()
            # # 将收集到的信息封装起来
            item['url'] = url
            item['sentence'] = sentence
            item['source'] = source
            # 处理子页
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_detail)

        next = response.xpath('//a[@class="amore"]/@href').get()
        if next is not None:
            next_url = 'https://so.gushiwen.cn' + next
            yield Request(next_url)

    def parse_detail(self, response):
        # 获取名句的详细信息
        item = response.meta['item']
        content_list = response.xpath('//div[@class="contson"]//text()').getall()
        content = "".join(content_list).strip().replace('\n', '').replace('\u3000', '')
        item['content'] = content
        yield item
