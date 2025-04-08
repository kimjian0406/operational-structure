from multiprocessing import Process  # 멀티 프로세스 프로그래밍을 위한 모듈
import os

# 자식 프로세스로 실행될 함수 정의
def func():
    print('안녕, 나는 실험용으로 대충 만들어 본 함수야!')
    print('나의 프로세스 아이디 (PID):', os.getpid())
    print('나의 부모 프로세스 아이디 (PPID):', os.getppid())  # PPID = Parent Process ID

# main 프로세스에서만 실행되도록 조건 설정
if __name__ == '__main__':
    print('os05.py의 프로세스 아이디 (PID):', os.getpid())  # 현재 실행 중인 메인 프로세스 ID 출력

    # 새로운 자식 프로세스를 생성하고 시작
    child = Process(target=func).start()

