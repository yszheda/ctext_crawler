# -*- coding: utf-8 -*-
import scrapy
from ctext.items import CtextItem


class QuantangshiSpider(scrapy.Spider):
    name = "quantangshi"
    allowed_domains = ["ctext.org"]
    start_urls = (
        'http://ctext.org/quantangshi/zh/',
    )

    def parse(self, response):
        for url in response.xpath('//div[@id="content2"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_volumn)

    def parse_volumn(self, response):
        for url in response.xpath('//h2/a/@href').extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_item)

    def parse_item(self, response):
        item = CtextItem()

        item['title'] = response.selector.xpath('//td/h2/text()').extract()[0]

        item['author'] = u"佚名"
        authors = response.selector.xpath('//td/span/b/text()').extract()
        if len(authors) > 0:
            item['author'] = "".join(authors)

        contents = response.xpath('//td[@class="ctext"]/text()').extract()
        item['content'] = "".join(contents)

        yield item
