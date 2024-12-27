# [Gold V] 숨바꼭질 3 - 13549 

[문제 링크](https://www.acmicpc.net/problem/13549) 

### 성능 요약

메모리: 34228 KB, 시간: 108 ms

### 분류

0-1 너비 우선 탐색, 너비 우선 탐색, 데이크스트라, 그래프 이론, 그래프 탐색, 최단 경로

### 제출 일자

2024년 11월 25일 01:38:31

### 문제 설명

<p>수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.</p>

<p>수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.</p>

### 출력 

 <p>수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.</p>

### 틀린 부분 
> 1. visited[nx] == 0으로 queue append 여부를 check하면서 K로 가는 여러가지 방법의 수를 계산하기 위해서 visited[K]를 True 처리 하지 않음 **min_t 계산이 안 됨**
~~~python
def bfs(start):
    n = 0
    min_t = 0
    visited[start] = True
    q = deque([(start, 0)])

    while q:
        x, times = q.popleft()

        if x == K:
            min_t = times
            n += 1

        for nx in (2*x, x-1, x+1):
            if in_range(nx) and not visited[nx]:
                q.append((nx, times+1))
                if nx != K:
                    visited[nx] = True

    return min_t, n
~~~


> 2. visited[nx] == visited[x] + 1 **방문한 지점이라도 방문한 시간이 같다면 방문할 수 있음**
~~~python
def bfs(start):
    n = 0
    visited[start] = True
    q = deque([start])

    while q:
        x = q.popleft()

        if x == K:
            n += 1
            continue

        for nx in (2*x, x-1, x+1):
            if in_range(nx) and (not visited[nx] or visited[nx] == visited[x] + 1):
                q.append(nx)
                visited[nx] = visited[x] + 1

    return n
~~~
