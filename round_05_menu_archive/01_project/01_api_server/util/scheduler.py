import threading
import schedule
import time




def start_scheduler(job, interval):
    schedule.every(interval).seconds.do(job)



# 스케줄러 실행 함수
# 대기중인 모든 스케줄을 실행하고 1초 대기
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)




# 스케줄러를 실행할 스레드 생성 및 시작
thread = threading.Thread(target=run_scheduler)
thread.start()

