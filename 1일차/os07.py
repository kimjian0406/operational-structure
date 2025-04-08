from multiprocessing import Process
import os
import time

# 각각 다른 음료를 흉내 내는 프로세스 함수들

def coke():
    print("[ Coke 프로세스 시작]")
    print("내 PID:", os.getpid())
    print("내 부모 PID:", os.getppid())
    print("-" * 30)

def cider():
    print("[ Cider 프로세스 시작]")
    print("내 PID:", os.getpid())
    print("내 부모 PID:", os.getppid())
    print("-" * 30)

def juice():
    print("[ Juice 프로세스 시작]")
    print("내 PID:", os.getpid())
    print("내 부모 PID:", os.getppid())
    print("-" * 30)

# 메인 프로세스에서 각각의 음료 프로세스를 실행
if __name__ == '__main__':
    print(" os07.py 메인 프로세스 PID:", os.getpid())
    print("각 음료 프로세스를 하나씩 만들어볼게요!\n")

    p1 = Process(target=coke)
    p1.start()
    time.sleep(0.5)

    p2 = Process(target=cider)
    p2.start()
    time.sleep(0.5)

    p3 = Process(target=juice)
    p3.start()
    time.sleep(0.5)

    print(" 모든 음료 프로세스를 실행했습니다!")

