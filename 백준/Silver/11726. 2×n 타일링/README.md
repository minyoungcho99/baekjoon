# [Silver III] 2×n 타일링 - 11726 

[문제 링크](https://www.acmicpc.net/problem/11726) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 11월 24일 18:05:10

### 문제 설명

<p>2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.</p>

<p>아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11726/1.png" style="height:50px; width:125px"></p>

### 입력 

 <p>첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)</p>

### 출력 

 <p>첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.</p>


### 틀린 부분 
~~~python
# 2xn 타일링
import sys

N = int(sys.stdin.readline())
D = [0] * (N + 1)
D[1], D[2] = 1, 2

if N == 1:
    print(1)

elif N == 2:
    print(2)

else:
    for i in range(3, N + 1):
        D[i] = (D[i - 1] + D[i - 2]) % 10007

    print(D[N])
~~~
**D[1], D[2]를 N을 생각하지 않고 assign해 IndexError가 발생함 (N = 1일 때, D[2]는 out of index) else에서만 D를 initialize 하고 index 1,2의 초기값을 주면서 해결**
