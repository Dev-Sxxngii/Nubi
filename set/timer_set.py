import datetime

class TimerSet:
    def __init__(self):
        self.current_datetime = None 
    

    ### 시간 저장 관련 기능
    # 현재 시간 업데이트 및 저장
    def update_current_datetime(self):
        self.current_datetime = datetime.datetime.now()


    ### 시간 정제 관련 기능
    # 현재 datetime 가져오기
    def get_current_datetime(self):
        return self.current_datetime.strftime("%y년%m월%d일_%H시%M분%S초")