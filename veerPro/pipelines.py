# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
from urllib.request import urlretrieve


class ImgsPipeLine(ImagesPipeline):

    # 根据图片地址发起请求
    def get_media_requests(self, item, info):
        print(item)
        urlretrieve(item['img_src'], r"F:\13.PycharmProjects(2017.2)\Casepractice\veerPro\imgLibs\{}.jpg".format(item['id']))


