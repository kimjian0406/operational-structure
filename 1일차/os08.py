# 실행 중인 프로세스 중 특정 파이썬 스크립트가 관련된 항목을 찾아보자

import psutil

target_script = "ex08.py"  # 확인하고 싶은 파이썬 스크립트 이름

print(f" '{target_script}'과 관련된 실행 중인 프로세스를 찾는 중...\n")

for proc in psutil.process_iter():
    try:
        # 현재 프로세스 이름
        name = proc.name()

        # 커맨드 라인 인자에 우리가 찾는 스크립트 이름이 포함되어 있는지 확인
        if target_script in " ".join(proc.cmdline()):
            print(f" 이름: {name}")
            print(f" 상태: {proc.status()}")
            print(f"‍ 부모 프로세스: {proc.parent()}")
            print(f" 자식 프로세스: {proc.children()}")
            print("-" * 40)

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

