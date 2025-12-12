from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

import random
import time

class DriverSet():
    def __init__(self):
        self.driver = None
        self.element = None
    
    ### driver 관련 기능
    # driver 열기
    def open_driver(self):
        self.driver = webdriver.Chrome()
        
    # driver 대기
    def wait_driver(self, css):
        self.element = WebDriverWait(self.driver, 10).until( # 명시적 대기
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css))
        )        

    # driver 종료
    def close_driver(self):
        self.driver.quit() 
           
    # driver 실행 여부 확인
    def is_driver_open(self):
        self.driver.current_url
        
    # url 주입
    def get_url(self, url):
        self.driver.get(url)
        self.driver.save_screenshot("headless_debug.png")
        
    
    ### driver 조작 관련 기능
    # 요소 찾기
    def find_element(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)

    # 요소(들) 찾기
    def find_elements(self, css):
        return self.driver.find_elements(By.CSS_SELECTOR, css)
    
    # 요소 속성 값 찾기
    def get_attribute(self, value, attribute):
        return value.get_attribute(attribute)

    # 요소 클릭        
    def click_element(self, css):
        self.driver.find_element(By.CSS_SELECTOR, css).click()          

    # 요소 입력
    def input_text(self, css, text):
        self.driver.find_element(By.CSS_SELECTOR, css).send_keys(text)        
        
    # PAGE_DOWN 입력
    def press_page_down(self):
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)

    # END 입력
    def press_end(self):
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # ENTER 클릭
    def press_enter(self, css):
        self.driver.find_element(By.CSS_SELECTOR, css).send_keys(Keys.ENTER)
    
    # 스크롤 이동
    def move_scroll(self, index):
        ActionChains(self.driver).move_to_element(self.element[index]).perform()              
        
    # 창 크기 조절
    def window_size_setting(self):
        self.driver.maximize_window() # 창 전체 크기


    ### 부가 기능
    # 랜덤 시간 생성
    def create_random_time(self):
        time.sleep(random.uniform(1, 2))