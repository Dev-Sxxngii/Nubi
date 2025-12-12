class ExcelController:    
    def __init__(self, excel_set, excel_env, timer_set, site, text):
        self.excel_set = excel_set
        self.excel_env = excel_env
        self.timer_set = timer_set
        self.site = site
        self.text = text
        self.file_name = ""
    
    # 파일 생성
    def setting_excel(self):
        default_sheet_name = self.excel_env["EXCEL_DEFAULT_SHEET_NAME"]
        start_time = self.timer_set.get_current_datetime()
        
        self.file_name = f"{self.site}_{self.text}"
        sheet_name = f"{self.site}_{self.text}_{start_time}"

        self.excel_set.create_file()
        self.excel_set.change_default_sheet_name(sheet_name, default_sheet_name)

    def save_excel(self, name):
        self.excel_set.save_file(name)