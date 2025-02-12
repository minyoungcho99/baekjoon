# [Silver II] A → B - 16953 

[문제 링크](https://www.acmicpc.net/problem/16953) 

### 성능 요약

메모리: 112088 KB, 시간: 120 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 그리디 알고리즘

### 제출 일자

2025년 2월 12일 16:44:33

### 문제 설명

<p>정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.</p>

<ul>
	<li>2를 곱한다.</li>
	<li>1을 수의 가장 오른쪽에 추가한다. </li>
</ul>

<p>A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.</p>

### 입력 

 <p>첫째 줄에 A, B (1 ≤ A < B ≤ 10<sup>9</sup>)가 주어진다.</p>

### 출력 

 <p>A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.</p>

### 틀린 부분 
### 틀린 부분 
> 1. visited 배열 사용 **109개의 수가 저장된 배열의 크기는, 하나의 수를 4B라고 가정해도 4000MB임**
~~~python
def bfs(start):
    visited[start] = 1
    q = deque([start])

    while q:
        x = q.popleft()

        if x == B:
            return visited[B]

        for nx in (2*x, int(str(x) + '1')):
            if nx <= B and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

    return -1
~~~


