# -*- coding: utf-8 -*-
import scrapy
from ctext.items import CtextItem


class Quantangshi1Spider(scrapy.Spider):
    name = "quantangshi1"
    allowed_domains = ["ctext.org"]
    start_urls = (
        'http://ctext.org/quantangshi/1/zh/',
    )

    def parse(self, response):
        for url in response.xpath('//h2/a/@href').extract():
            yield scrapy.Request(response.urljoin(url), callback=self.parse_item)

    def parse_item(self, response):
        item = CtextItem()
        item['title'] = response.selector.xpath('//td/h2/text()').extract()[0]
        item['author'] = response.selector.xpath('//td/span/b/text()').extract()[0]
        contents = response.xpath('//td[@class="ctext"]/text()').extract()
        item['content'] = "".join(contents)
        yield item
