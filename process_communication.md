# 프로세스 통신과 동기화

## 프로세스 통신 (IPC: Inter-Process Communication)

- 파이프 (Pipe)
- 메시지 큐 (Message Queue)
- 공유 메모리 (Shared Memory)
- 소켓 (Socket)

## 동기화 (Synchronization)

- 임계 구역 (Critical Section)
- 세마포어 (Semaphore)
- 뮤텍스 (Mutex)

## 예시 코드

```python
# 예시: 세마포어를 이용한 간단한 동기화
from multiprocessing import Semaphore, Process
import time

sem = Semaphore(1)

def task(name):
    sem.acquire()
    print(f"{name} 작업 시작")
    time.sleep(2)
    print(f"{name} 작업 완료")
    sem.release()

if __name__ == '__main__':
    p1 = Process(target=task, args=("프로세스 1",))
    p2 = Process(target=task, args=("프로세스 2",))
    p1.start()
    p2.start()

