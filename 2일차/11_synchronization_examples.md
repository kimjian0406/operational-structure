# 동기화 추가 예제

##  예제 1: 뮤텍스를 이용한 카운터 증가

```c
#include <pthread.h>
#include <stdio.h>

int count = 0;
pthread_mutex_t lock;

void* increment(void* arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&lock);
        count++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&lock, NULL);

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("최종 카운트: %d\n", count);
    pthread_mutex_destroy(&lock);
    return 0;
}

#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

sem_t sem;

void* access_resource(void* arg) {
    sem_wait(&sem); // 자원 접근 허용 대기
    printf("스레드 %ld: 자원 사용 중\n", (long)arg);
    sleep(1);
    printf("스레드 %ld: 자원 사용 종료\n", (long)arg);
    sem_post(&sem); // 자원 반납
    return NULL;
}

int main() {
    pthread_t threads[5];
    sem_init(&sem, 0, 2); // 동시에 2개 스레드만 자원 접근 가능

    for (long i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, access_resource, (void*)i);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&sem);
    return 0;
}

