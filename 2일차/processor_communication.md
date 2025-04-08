# 프로세서 간 통신 (Processor Communication)

##  개요
멀티 프로세서 시스템이나 멀티코어 환경에서 서로 다른 프로세서들이 어떻게 데이터를 교환하고 협력하는지를 설명합니다.

---

##  주요 개념

### 1. 공유 메모리 방식
- 여러 프로세서가 공통 메모리 공간을 사용하여 통신
- 장점: 빠른 속도
- 단점: 동기화 문제, 레이스 컨디션 발생 가능성

### 2. 메시지 전달 방식
- 각 프로세서가 독립적인 메모리 공간을 갖고 있으며, 메시지를 통해 통신
- 시스템 간 통신 (IPC)와 유사
- 장점: 안정성, 충돌 방지
- 단점: 오버헤드 발생 가능

---

##  예시

```python
# 예: 파이썬 multiprocessing에서 Queue를 통한 통신
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from worker!")

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()

