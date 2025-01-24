# [Silver II] 종이의 개수 - 1780 

[문제 링크](https://www.acmicpc.net/problem/1780) 

### 성능 요약

메모리: 163560 KB, 시간: 1976 ms

### 분류

분할 정복, 재귀

### 제출 일자

2025년 1월 24일 20:03:01

### 문제 설명

<p>N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.</p>

<ol>
	<li>만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.</li>
	<li>(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.</li>
</ol>

<p>이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 3<sup>7</sup>, N은 3<sup>k</sup> 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.</p>

### 출력 

 <p>첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.</p>

### 틀린 부분 
> 1. split_paper(0, 0, int((math.log(N, 3))) # call **부동소수점 오류**
~~~python
# 종이의 개수
import sys
import math

N = int(sys.stdin.readline())
paper = []

neg = 0
zero = 0
pos = 0

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def check(sx, sy, d):
    temp = paper[sx][sy]
    for i in range(sx, sx + 3**d):
        for j in range(sy, sy+ 3**d):
            if paper[i][j] != temp:
                return 2

    return temp


def split_paper(sx, sy, d):
    global neg, zero, pos

    if check(sx, sy, d) != 2:
        if check(sx, sy, d) == -1:
            neg += 1

        elif check(sx, sy, d) == 0:
            zero += 1

        else:
            pos += 1
        return

    # recursive call
    split_paper(sx, sy, d - 1)
    split_paper(sx + 3**(d - 1), sy, d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy, d - 1)

    split_paper(sx, sy + 3**(d - 1), d - 1)
    split_paper(sx + 3**(d - 1), sy + 3**(d - 1), d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy + 3**(d - 1), d - 1)

    split_paper(sx, sy + 2 * 3**(d - 1), d - 1)
    split_paper(sx + 3**(d - 1), sy + 2 * 3**(d - 1), d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy + 2 * 3**(d - 1), d - 1)


split_paper(0, 0, int(math.log(N, 3))) # call
print(neg)
print(zero)
print(pos)
~~~
재귀 레벨에 맞춰 인덱싱을 해주기 위해 split_paper(0, 0, int(math.log(N, 3)))로 인덱싱했음, len(curr_arr)이 243을 넘어가는 순간 5가 아니라 4.99999... 로 나와서 int()를 씌워주면 0.9999... 값이 버려짐 -> 해결하기 위해서 **int(round(math.log(N, 3))** 하거나 정수 계산 해줌 **N //= 3**

### 고친다면 
~~~python
import sys

N = int(sys.stdin.readline())
paper = []

neg = 0
zero = 0
pos = 0

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def check(sx, sy, size):
    temp = paper[sx][sy]
    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if paper[i][j] != temp:
                return 2

    return temp


def split_paper(sx, sy, size):
    global neg, zero, pos

    if check(sx, sy, size) != 2:
        if check(sx, sy, size) == -1:
            neg += 1

        elif check(sx, sy, size) == 0:
            zero += 1

        else:
            pos += 1
        return

    # 분할 재귀
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            split_paper(sx + i * new_size, sy + j * new_size, new_size)


split_paper(0, 0, N)  # N을 그대로 사용
print(neg)
print(zero)
print(pos)
~~~
