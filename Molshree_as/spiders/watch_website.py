import scrapy


class WatchWebsiteSpider(scrapy.Spider):
    name = 'watch_website'
    allowed_domains = ['www.watchfinder.co.uk']
    start_urls = ['https://www.watchfinder.co.uk/Rolex/Datejust/116200/9774/item/246574']

    def parse(self, response):

        brand = response.xpath("(//div[@class='product--details']/h1/span[1]/text())[1]").get()
        name = response.xpath("(//div[@class='product--details']/h1/span[2]/text())[1]").get()
        modelNo= response.xpath("(//div[@class='product--details']/h1/span[3]/text())[1]").get()
        price = response.xpath("//div[@class='product--details']/span/text()").get()
        box = response.xpath("//div[@id='specification-content']/table/tbody/tr[1]/td[2]/text()").get()
        papers = response.xpath("//div[@id='specification-content']/table/tbody/tr[2]/td[2]/text()").get()
        year = response.xpath("//div[@id='specification-content']/table/tbody/tr[3]/td[2]/text()").get()
        product_code= response.xpath("//div[@id='specification-content']/table/tbody/tr[4]/td[2]/text()").get()
        watchFinder_warranty = response.xpath("//div[@id='specification-content']/table/tbody/tr[5]/td[2]/text()").get()
        case_size= response.xpath("//div[@id='specification-content']/table/tbody/tr[6]/td[2]/text()").get()
        case_material= response.xpath("//div[@id='specification-content']/table/tbody/tr[7]/td[2]/text()").get()
        movement= response.xpath("//div[@id='specification-content']/table/tbody/tr[8]/td[2]/text()").get()
        bracelet_material= response.xpath("//div[@id='specification-content']/table/tbody/tr[9]/td[2]/text()").get()
        dial_type= response.xpath("//div[@id='specification-content']/table/tbody/tr[10]/td[2]/text()").get()
        water_resistance= response.xpath("//div[@id='specification-content']/table/tbody/tr[11]/td[2]/text()").get()
        location= response.xpath("//div[@id='specification-content']/table/tbody/tr[12]/td[2]/text()").get()
        yield{
            'brand':brand,
            'name':name,
            'modelNo':modelNo,
            'price':price,
            'box':box,
            'papers':papers,
            'year':year,
            'product_code':product_code,
            'watchFinder_warranty':watchFinder_warranty,
            'case_size':case_size,
            'case_material':case_material,
            'movement':movement,
            'bracelet_material':bracelet_material,
            'dial_type':dial_type,
            'water_resistance':water_resistance,
            'location':location
        }
