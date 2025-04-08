#  CPU 스케줄링

##  CPU 스케줄링이란?
운영체제가 어떤 프로세스에게 CPU를 할당할지를 결정하는 방식입니다.

---

##  대표적인 스케줄링 알고리즘

1. **FCFS (First Come First Served)**  
   - 먼저 도착한 프로세스에게 CPU를 먼저 할당합니다.

2. **SJF (Shortest Job First)**  
   - 실행 시간이 가장 짧은 프로세스를 우선으로 실행합니다.

3. **Priority Scheduling**  
   - 우선순위가 높은 프로세스에게 먼저 CPU를 할당합니다.

4. **Round Robin (RR)**  
   - 시간 할당량(Time Quantum)을 정해, 모든 프로세스에게 공평하게 CPU를 순환시킵니다.

5. **MLFQ (Multi-Level Feedback Queue)**  
   - 여러 개의 큐를 사용해 다양한 특성을 가진 프로세스를 처리합니다.

---

##  스케줄링 기준
- 응답 시간
- 대기 시간
- 처리 시간
- CPU 사용률

---

##  예시 코드 (Python)

> 간단한 Round Robin 시뮬레이션 예제

```python
# 실제 OS의 동작과는 다르지만 기본 개념 설명용 코드
processes = ['P1', 'P2', 'P3']
time_quantum = 2
queue = processes.copy()

while queue:
    p = queue.pop(0)
    print(f"{p} 실행 중 (할당된 시간: {time_quantum})")
    # 실제로는 남은 실행 시간이 있다면 다시 큐에 삽입

