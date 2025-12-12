from set.timer_set import TimerSet
from controller.timer_controller import TimerController

from set.driver_set import DriverSet
from controller.driver_controller import DriverController

from set.excel_set import ExcelSet
from controller.excel_controller import ExcelController

from controller.crawler_controller import CrawlerController

from controller.env_controller import split_env_by_category

class DependencyContainer:
    def __init__(self, site, text, page):
        self.timer_set = TimerSet()
        self.driver_set = DriverSet()
        self.excel_set = ExcelSet()
        self.site = site
        self.text = text
        self.page = page

    def time_injection(self):
        return TimerController(self.timer_set)
    
    def driver_injection(self):
        return DriverController(self.driver_set, split_env_by_category(self.site), self.site, self.text)
    
    def excel_injection(self):
        return ExcelController(self.excel_set, split_env_by_category("EXCEL"), self.timer_set, self.site, self.text)
    
    def crawler_injection(self):
        return CrawlerController(self.driver_set, split_env_by_category(self.site), self.excel_set, self.site, self.page)