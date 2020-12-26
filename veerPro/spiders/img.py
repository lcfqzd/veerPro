import scrapy
from ..items import VeerproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['xxx.com']
    start_urls = ['https://www.veer.com/topic/1027/?page=1']

    # 通用url模板
    url = 'https://www.veer.com/topic/1027/?page=%d'
    page_num = 2

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        # 解析a链接
        a_list = response.xpath('//*[@id="root"]/div/div[5]/div/article/section[2]/div/div/article/section/section/a')

        hrefs = []

        for a in a_list:
            item = VeerproItem()

            href = a.xpath('./@href').extract_first()
            hrefs.append(href)

        # print(hrefs)
        for href in hrefs[1:]:
            print(href)
            yield scrapy.Request(url=href, callback=self.parse_img_src)

        if self.page_num < 7:
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)

            self.page_num += 1

    def parse_img_src(self, response):
        item = {}
        img_src = response.xpath('//div[@class="unzoomed"]/img/@src').extract_first()
        item['img_src'] = 'https:' + img_src
        id = img_src.split('-')[-1].split('.')[0]

        item['id'] = id

        yield item
