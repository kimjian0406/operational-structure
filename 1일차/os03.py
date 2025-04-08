# pip3 install psutil
# psutil은 실행 중인 프로세스 정보를 조회하고 관리할 수 있는 유용한 라이브러리입니다.

import psutil

# 내 컴퓨터에서 실행 중인 프로세스 목록을 순회하며 확인
for proc in psutil.process_iter():
    try:
        # 프로세스 이름 가져오기
        process_name = proc.name()

        # 예: 실행 중인 프로세스 이름 중에 'chrome'이 포함된 경우 출력
        if "chrome" in process_name.lower():
            print(f"프로세스 이름: {process_name}, PID: {proc.pid}")

    # 접근 권한 문제나 이미 종료된 프로세스는 예외 처리
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

