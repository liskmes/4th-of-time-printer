import time
import os

def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

while True:
    current_time = time.strftime('%H:%M:%S')  # 获取当前时间
    clear_screen()                            # 清除屏幕内容
    print(f"Current Time: {current_time}")    # 打印当前时间
    time.sleep(1)                             # 等待一秒钟