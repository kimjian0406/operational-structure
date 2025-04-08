# 프로세스 간 통신 (Inter-Process Communication, IPC)

운영체제에서는 하나의 프로그램이 여러 프로세스를 생성하여 동시에 실행할 수 있습니다.  
이러한 프로세스들끼리는 **데이터 공유**나 **작업 협력**이 필요할 수 있습니다. 이를 위해 사용되는 방식이 **IPC (Inter-Process Communication)** 입니다.

---

##  IPC의 필요성

- 서로 다른 프로세스가 데이터를 공유해야 할 때
- 클라이언트와 서버 간 통신
- 여러 작업을 동시에 처리하고 결과를 하나로 합칠 때

---

##  주요 통신 방식

### 1. **파이프 (Pipe)**
- 단방향 통신
- 부모와 자식 프로세스 간에 사용
- `|` 연산자로도 사용 가능 (리눅스 셸)

### 2. **FIFO (Named Pipe)**
- 이름이 있는 파이프
- 서로 관계없는 프로세스들 간 통신 가능

### 3. **메시지 큐 (Message Queue)**
- 운영체제 커널이 메시지를 저장
- 큐 형태로 메시지를 주고받음

### 4. **공유 메모리 (Shared Memory)**
- 메모리 공간을 공유하여 데이터를 교환
- 빠르지만 동기화 문제가 있음

### 5. **소켓 (Socket)**
- 네트워크를 통한 IPC
- 로컬 혹은 원격 프로세스 간 통신 가능

---

##  동기화 도구

- 세마포어 (Semaphore)
- 뮤텍스 (Mutex)
- 조건 변수 (Condition Variable)

---

##  예시 상황

- 크롬에서 여러 탭이 서로 상태를 주고받을 때
- 게임 서버에서 클라이언트가 로그인 요청을 보내고 서버가 응답할 때

---

## ️ 파이썬에서 IPC 예시

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send(['Hello', 42, None])
    conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
print(parent_conn.recv())  # ['Hello', 42, None]
p.join()

