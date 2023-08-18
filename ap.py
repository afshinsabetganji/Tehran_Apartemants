
import scrapy
import requests
import re
from unidecode import unidecode



with open('Tokens_Location\elahiyeh.txt', 'r', encoding='utf8') as texts:
    tokens = texts.read().split(',')
    
    
url = 'https://divar.ir/v/{token}'


class a_crawl_spider(scrapy.Spider):

    name = 'aparteman'
    start_urls = [

                        url.format(token = i)  for i in tokens

    ]
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }

    def parse(self, response):
        print('|**|'*120)
        info = response.css(
            'div span.kt-group-row-item__value::text').extract()
        area = (info[0])
        year = (info[1])
        rooms = (info[2])
        warehouse = 20 if 'ندارد' in info[3] else 100
        parking = 10 if 'ندارد' in info[4] else 350
        asansor = 10 if 'ندارد' in info[5] else 250

        p = response.css('div p.kt-unexpandable-row__value::text').extract()
        a = re.sub(r',', '', p[0])
        a = re.sub(r'تومان', '', a)
        price = unidecode(a)
        price = re.sub(r',', '', price)
        Floor = 100000
        pp = p[3]
        if p[3] == 'همکف':
            Floor = 0
        elif (pp[0].isdigit()):
            Floor = int(unidecode(pp[0]))
        else:
            Floor = -1
        if year == 'qbl z 1370':
            year = 1365
        pricepermetr = int(price)/int(area)
        print('|**|'*120)
        print(Floor)
        yield {
            'address': 1000,
            'Area': int(area),
            'year': int(year),
            'rooms': int(rooms),
            'Floor': int(Floor),
            'warehouse':int(warehouse),
            'parking': int(parking),
            'asansor': int(asansor),
            'ppm': int(pricepermetr),
            'price': int(price)
        }
