# 동기화(Synchronization)

멀티프로세스 및 멀티스레드 환경에서의 동기화는 여러 프로세스 혹은 스레드가 **공유 자원에 동시에 접근하는 것을 제어**하기 위해 꼭 필요합니다.

##  왜 필요한가요?

- **경쟁 조건(Race Condition)**: 둘 이상의 프로세스/스레드가 동시에 자원에 접근하면, 예상치 못한 결과 발생 가능
- **데이터 무결성(Data Integrity)** 보장을 위해 필요

##  주요 동기화 도구

- **뮤텍스(Mutex)**
- **세마포어(Semaphore)**
- **모니터(Monitor)**
- **락(Lock)**

##  코드 예시 (파이썬)

```python
import threading

count = 0
lock = threading.Lock()

def increase():
    global count
    for _ in range(100000):
        lock.acquire()
        count += 1
        lock.release()

threads = []

for _ in range(2):
    t = threading.Thread(target=increase)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("최종 카운트:", count)

