class DriverController:    
    def __init__(self, driver_set, driver_env, site, text):
        self.driver_set = driver_set
        self.driver_env = driver_env
        self.site = site
        self.text = text
    
    # 드라이버 열기
    def open_driver(self):
        url = self.driver_env[f"{self.site}_URL"]
        self.driver_set.open_driver()
        # self.driver_set.get_url(url)
        # self.driver_set.create_random_time()
        
    # 상품 검색
    def search_product(self):
        css = self.driver_env[f"{self.site}_SEARCH_ELEMENT"]
        self.driver_set.click_element(css)
        self.driver_set.input_text(css, self.text)
        self.driver_set.press_enter(css)
    
    # 드라이버 대기
    def wait_to_driver(self):
        css = self.driver_env[f"{self.site}_SEARCH_ELEMENT"]
        try:
            self.driver_set.wait_driver(css)
        except TimeoutError:
            self.driver_set.close_driver()

    # 드라이버 총괄
    def setup_driver(self):
        self.open_driver()
        # self.wait_to_driver()
        self.driver_set.create_random_time()
        self.driver_set.window_size_setting()
        self.search_product()