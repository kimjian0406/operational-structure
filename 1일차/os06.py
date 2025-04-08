from multiprocessing import Process  # 멀티 프로세스 생성을 위한 모듈
import os
import time

# 자식 프로세스에서 실행할 함수 정의
def experiment():
    print(" 자식 프로세스 실행 중!")
    print("PID (내 ID):", os.getpid())
    print("PPID (부모 ID):", os.getppid())
    print("-" * 30)

# 메인 프로세스의 실행 구간
if __name__ == '__main__':
    print(" 메인 프로세스 시작! PID:", os.getpid())
    print("자식 프로세스를 하나씩 생성해볼게요...\n")

    # 첫 번째 자식 프로세스
    p1 = Process(target=experiment)
    p1.start()
    time.sleep(0.5)  # 간단한 텀을 줘서 출력 구분

    # 두 번째 자식 프로세스
    p2 = Process(target=experiment)
    p2.start()
    time.sleep(0.5)

    # 세 번째 자식 프로세스
    p3 = Process(target=experiment)
    p3.start()
    time.sleep(0.5)

    print(" 모든 자식 프로세스를 실행했습니다!")

