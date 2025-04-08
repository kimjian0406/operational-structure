# 동기화 (Synchronization)

##  개요
- 동기화는 여러 프로세스나 스레드가 공유 자원에 동시에 접근할 때 발생할 수 있는 문제(경쟁 상태)를 방지하기 위한 기술입니다.

---

##  핵심 개념

###  경쟁 상태 (Race Condition)
- 두 개 이상의 프로세스가 동시에 자원에 접근하여 결과가 예측 불가능하게 되는 상황.

###  임계 구역 (Critical Section)
- 여러 프로세스가 공유 자원에 접근하는 코드의 영역.
- 한 번에 하나의 프로세스만 임계 구역에 들어갈 수 있어야 함.

---

##  동기화 도구

### 1. 뮤텍스 (Mutex)
- 상호 배제를 보장하기 위한 가장 기본적인 도구.
- 한 번에 하나의 프로세스만 자원에 접근 가능하게 함.

```c
pthread_mutex_t lock;

pthread_mutex_lock(&lock);
// 공유 자원 접근
pthread_mutex_unlock(&lock);

sem_t sem;

sem_wait(&sem); // P 연산
// 임계 구역
sem_post(&sem); // V 연산
synchronized void criticalSection() {
    // 임계 구역
}

from threading import Thread

count = 0

def increment():
    global count
    for _ in range(100000):
        count += 1

threads = [Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print("최종 count:", count)

