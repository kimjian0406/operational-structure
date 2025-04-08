import psutil

# process_iter(): 실행 중인 모든 프로세스를 반복적으로 접근할 수 있는 함수
for proc in psutil.process_iter():
    try:
        ps_name = proc.name()

        # 크롬은 여러 개의 하위 프로세스로 실행되므로 그 구조를 확인할 수 있음
        if "Chrome" in ps_name:
            # 자식 프로세스 가져오기
            children = proc.children()

            # 프로세스 이름, 상태, 부모 프로세스, 자식 프로세스 출력
            print(f"이름: {ps_name}")
            print(f"상태: {proc.status()}")
            print(f"부모 프로세스: {proc.parent()}")
            print(f"자식 프로세스: {children}")
            print('-' * 40)

            if children:
                print(f" {ps_name}은 자식 프로세스를 가지고 있습니다.")
                print()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 프로세스가 이미 종료되었거나 접근이 불가능할 경우 무시
        continue

