# IPC (Inter-Process Communication) 예제

여러 프로세스가 서로 데이터를 주고받기 위해 IPC를 활용합니다.  
파이썬에서는 `multiprocessing` 모듈의 `Pipe`, `Queue` 등을 사용해 구현할 수 있어요.

---

##  예제 1: 파이프 (Pipe)

파이프는 양방향 통신이 가능합니다.

```python
from multiprocessing import Process, Pipe

def worker(conn):
    data = conn.recv()
    print("자식 프로세스가 받은 메시지:", data)
    conn.send("응답: 잘 받았어!")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    parent_conn.send("안녕? 데이터 보낸다~")
    print(parent_conn.recv())
    p.join()
from multiprocessing import Process, Queue

def worker(q):
    q.put('Hello from child process')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # 'Hello from child process'
    p.join()

