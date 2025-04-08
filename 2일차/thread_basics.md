# 스레드의 이해

##  스레드란?

- 프로세스 내에서 실행되는 **작은 실행 단위**.
- 하나의 프로세스 안에서 여러 스레드를 생성해 **병렬 처리**가 가능하다.
- 스레드들은 **코드, 데이터, 파일 등 자원**을 공유한다.

##  특징

- **가볍다**: 프로세스를 새로 만드는 것보다 비용이 적다.
- **자원 공유**: 같은 프로세스의 메모리 공간을 공유한다.
- **독립 실행 불가**: 프로세스 없이 스레드만 존재할 수 없다.

##  스레드 사용 예시

- 웹 서버: 여러 요청을 동시에 처리할 때
- 게임: 그래픽 렌더링, 사용자 입력 등을 각각 처리

##  예제 코드 (Python)

```python
import threading
import time

def greet(name):
    print(f"{name} 스레드 시작!")
    time.sleep(2)
    print(f"{name} 스레드 종료!")

t1 = threading.Thread(target=greet, args=("A",))
t2 = threading.Thread(target=greet, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("모든 스레드 종료 완료")

