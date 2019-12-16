# schedule

# 引入/导入schedule、time
import schedule, time


# 定义一个叫job的函数，
# 该函数的功能是打印"Working in progress...(程序正在运行。。。)"
def job():
    print("Working in progress...")


# 没0.01分钟执行一次job()函数的任务
schedule.every(0.1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
