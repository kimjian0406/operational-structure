# 동기화 (Synchronization)

운영체제에서 "동기화"는 여러 프로세스나 스레드가 자원을 공유할 때 **충돌 없이** 작업을 수행하게 만드는 것을 의미합니다.

##  왜 동기화가 필요할까?

공유 자원(파일, 변수 등)을 동시에 접근하면 **경쟁 조건(Race Condition)** 이 발생할 수 있음. 이럴 때 동기화 기법으로 문제를 방지함.

---

##  주요 동기화 도구

### 1. 뮤텍스(Mutex)
- 상호 배제를 보장하는 잠금 장치
- 한 번에 하나의 스레드만 자원 접근 가능

```python
import threading

lock = threading.Lock()

shared_data = 0

def task():
    global shared_data
    for _ in range(100000):
        lock.acquire()
        shared_data += 1
        lock.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()
t1.join()
t2.join()

print("최종 값:", shared_data)

import threading
import time

sem = threading.Semaphore(3)

def bathroom(user):
    print(f"{user} 대기 중")
    with sem:
        print(f"{user} 사용 중 🚽")
        time.sleep(2)
        print(f"{user} 나감")

for i in range(5):
    t = threading.Thread(target=bathroom, args=(f"User-{i}",))
    t.start()

