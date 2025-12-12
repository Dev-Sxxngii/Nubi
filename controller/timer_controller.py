class TimerController:
    def __init__(self, timer_set):
        self.timer_set = timer_set
    
    
    # 시작 시간 출력
    def update_time(self):
        self.timer_set.update_current_datetime()