# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from proxy.items import ProxyItem


MAX_PAGE = 2

class ProxyspiderSpider(Spider):
    name = "proxySpider"
    allowed_domains = ["kuaidaili.com"]
    start_urls = []

    def start_requests(self):
        url_head = 'http://www.kuaidaili.com/free/outha/{page}/'
        for i in range(1, MAX_PAGE):
            url = url_head.format(page=i)
            print url
            self.start_urls.append(url)

        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        hxs = Selector(response)
        contents = hxs.xpath('//*[@id="list"]//table')

        item = ProxyItem()
        for content in contents:
            for i in range(2, 17):
                item['ip'] = content.xpath('//tr[%s]//td[1]/text()' %i).extract()
                item['port'] = content.xpath('//tr[%s]//td[2]/text()' %i).extract()
                item['status'] = content.xpath('//tr[%s]//td[3]/text()' %i).extract()
                item['type'] = content.xpath('//tr[%s]//td[4]/text()' %i).extract()
                item['address'] = content.xpath('//tr[%s]//td[5]/text()' %i).extract()
                item['speed'] = content.xpath('//tr[%s]//td[6]/text()' %i).extract()
                item['last_validate_time'] = content.xpath('//tr[%s]//td[7]/text()' %i).extract()
                yield item
