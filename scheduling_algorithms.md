# 스케줄링 알고리즘

운영체제에서 프로세스를 효율적으로 실행시키기 위한 CPU 스케줄링 알고리즘을 설명합니다.

---

## 1. 비선점 스케줄링 (Non-preemptive Scheduling)

###  FCFS (First Come First Serve)
- 가장 먼저 도착한 프로세스부터 실행.
- **장점**: 구현이 간단.
- **단점**: Convoy effect 발생 가능.

###  SJF (Shortest Job First)
- 실행 시간이 가장 짧은 프로세스를 먼저 실행.
- **장점**: 평균 대기 시간 최소화.
- **단점**: 실행 시간을 미리 알아야 함.

---

## 2. 선점 스케줄링 (Preemptive Scheduling)

###  Round Robin (RR)
- 시간 할당량(Time Quantum)을 설정하여 프로세스를 순환 실행.
- **장점**: 응답 시간이 균형잡힘.
- **단점**: Time Quantum이 너무 작거나 크면 비효율 발생.

###  SRTF (Shortest Remaining Time First)
- 실행 시간이 가장 적게 남은 프로세스 우선.
- SJF의 선점형 버전.

###  Priority Scheduling
- 우선순위가 높은 프로세스 먼저 실행.
- **단점**: Starvation 발생 가능 → Aging 기법으로 해결 가능.

---

## 3. 실시간 스케줄링 (Real-time Scheduling)
- 하드 실시간 & 소프트 실시간 시스템에서 사용.
- 예) Rate Monotonic, EDF(Earliest Deadline First)

---

##  참고
- 스케줄링 알고리즘은 시스템 특성에 따라 선택되어야 함.
- 선점 여부, 평균 대기 시간, 응답 시간 등을 고려.


