# 프로세스 간 통신 (Interprocess Communication, IPC)

##  개요
IPC는 독립적인 프로세스들이 정보를 주고받는 방법입니다. 운영체제는 다양한 IPC 메커니즘을 제공하여 프로세스 간 협업을 지원합니다.

---

##  IPC 메커니즘

### 1. 파이프 (Pipe)
- 단방향 통신, 부모-자식 간 통신에서 주로 사용

### 2. 메시지 큐 (Message Queue)
- 커널이 관리하는 큐를 통해 메시지를 주고받음

### 3. 공유 메모리 (Shared Memory)
- 메모리 공간을 공유하여 빠른 데이터 전송 가능
- 동기화 기법 필요

### 4. 소켓 (Socket)
- 네트워크를 통한 통신. 로컬 또는 원격 프로세스 간 통신 가능

---

##  예시

```python
# 예: 파이썬에서 파이프를 이용한 IPC
from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Message from child")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

