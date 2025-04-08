# 프로세스 간 통신 - 추가 예제

##  목적
IPC(Interprocess Communication)에 대한 다양한 실습 예제를 통해 개념을 명확히 이해하고 응용력을 키웁니다.

---

##  예제 1: 파이프를 이용한 프로세스 간 통신

```python
from multiprocessing import Process, Pipe

def send_data(conn):
    conn.send("데이터 전송 완료!")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=send_data, args=(child_conn,))
    p.start()
    print("수신된 메시지:", parent_conn.recv())
    p.join()

from multiprocessing import Process, Value

def increment(val):
    for _ in range(10000):
        val.value += 1

if __name__ == "__main__":
    num = Value('i', 0)
    p1 = Process(target=increment, args=(num,))
    p2 = Process(target=increment, args=(num,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("최종 값:", num.value)

# 서버
import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)

conn, addr = server.accept()
data = conn.recv(1024)
print("받은 데이터:", data.decode())
conn.close()

# 클라이언트 (다른 파일 또는 터미널에서 실행)
import socket

client = socket.socket()
client.connect(('localhost', 9999))
client.send("Hello from client".encode())
client.close()

