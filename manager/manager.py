from dependency import DependencyContainer
from controller.env_controller import load_env

def manager(site, text, page):
    load_env()
    
    dependency = DependencyContainer(site, text, page)
    dependency.time_injection().update_time()
    dependency.driver_injection().setup_driver()
    excel_controller = dependency.excel_injection()
    excel_controller.setting_excel()
    dependency.crawler_injection().setup_crawler()
    return excel_controller
