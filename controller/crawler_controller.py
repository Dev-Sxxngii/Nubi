import re

class CrawlerController:
    def __init__(self, driver_set, driver_env, excel_set, site, page):
        self.driver_set = driver_set
        self.driver_env = driver_env
        self.excel_set = excel_set
        self.site = site
        self.page = page
        self.crawl_data_list = []
        self.product_id_list = []


    def product_data_processing(self, productInfo):
        productInfo = productInfo.replace('해외', '해외\n').replace('\n원\n', '원\n').replace('리뷰 ','\n')
        productInfo = re.sub(r"(해당 상품 찜하기|품절임박\n|배송비|면제\n?|별점\n|숏클립\n|공식\n|최저가\n)", "", productInfo) # 참고 사이트: https://luvris2.tistory.com/852
        productInfo = re.sub(r"할인[ \w\n,%]+할인\n", "", productInfo)
        productInfo = re.sub(r"오늘[\w :]+\n?", "", productInfo)
        productInfo = re.sub(r"원.*", "원", productInfo, flags=re.DOTALL)
        return productInfo

    
    # 중복 상품 제거 예외처리
    # def find_same_product(self, load_product_data):
    def find_same_product(self, load_product_data):
        self.driver_set.create_random_time
        product_meta = self.driver_set.find_elements(f'#composite-card-list > div > ul.compositeCardList_product_list__Ih4JR > li:nth-child({1}) > div > a')
        product_id = self.driver_set.get_attribute(product_meta[0], 'aria-labelledby')
        weight_index = 0
        if product_id in self.product_id_list:
            current_index = self.product_id_list.index(product_id)
            if load_product_data <= 100:
                weight_index = len(self.product_id_list) - current_index
            else:
                weight_index = len(self.product_id_list) - current_index + 1
        return weight_index     
    

    def crawl(self):
        while self.page > len(self.crawl_data_list):

            self.driver_set.create_random_time()
            self.driver_set.press_end()
            
            load_product_data = self.driver_set.find_elements(f'#composite-card-list > div > ul.compositeCardList_product_list__Ih4JR > li')
                
            repeat_count = len(load_product_data)

            if(self.page < len(self.crawl_data_list) + len(load_product_data)):
                repeat_count = self.page - len(self.crawl_data_list)

            weight_index = self.find_same_product(len(load_product_data))

            self.driver_set.create_random_time()
            for i in range(repeat_count):
                try:
                    product_meta = self.driver_set.find_elements(f'#composite-card-list > div > ul.compositeCardList_product_list__Ih4JR > li:nth-child({i + 1 + weight_index}) > div > a')
                    product_id = self.driver_set.get_attribute(product_meta[0], 'aria-labelledby')
                    self.product_id_list.append(product_id)
                    product_url = self.driver_set.get_attribute(product_meta[0], 'href')
                    raw_data = self.driver_set.find_elements(f'#{product_id}')[0].text
                    product_data = self.product_data_processing(raw_data)
                    product_data_list = product_data.split('\n')

                    if product_data_list[-1] == "":
                        del product_data_list[-1]

                    if "해외" not in product_data_list and "광고" not in product_data_list:
                        product_data_list.insert(0, "일반")
                        del product_data_list[1]
                    elif "해외" in product_data_list:
                        product_index = product_data_list.index("해외")
                        del product_data_list[product_index - 1]
                    elif "광고" in product_data_list:
                        product_index = product_data_list.index("광고")
                        del product_data_list[product_index + 1]

                    product_data_list.append(product_url)

                    self.crawl_data_list.append(product_data_list)

                except IndexError:
                    pass
    

    def write_to_excel(self):
        data = ['타입', '상품명', '가격', '하이퍼링크']
        for i in range(len(data)):
            self.excel_set.ws.cell(row=1, column=i + 1).value = data[i]

        for i in range(len(self.crawl_data_list)):
            for j in range(len(self.crawl_data_list[i])):
                self.excel_set.ws.cell(row=i + 2, column=j + 1).value = self.crawl_data_list[i][j]
            self.excel_set.ws.cell(row=i + 2, column=j + 1).hyperlink = self.crawl_data_list[i][j]
            self.excel_set.ws.cell(row=i + 2, column=j + 1).value = 'url'
            self.excel_set.ws.cell(row=i + 2, column=j + 1).style = 'Hyperlink'

    
    def setup_crawler(self):
        self.crawl()
        self.write_to_excel()
        self.driver_set.close_driver()


