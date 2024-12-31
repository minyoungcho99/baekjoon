# [Gold IV] 부분합 - 1806 

[문제 링크](https://www.acmicpc.net/problem/1806) 

### 성능 요약

메모리: 42168 KB, 시간: 112 ms

### 분류

누적 합, 두 포인터

### 제출 일자

2024년 12월 31일 00:34:51

### 문제 설명

<p>10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.</p>

### 출력 

 <p>첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.</p>

### 틀린 부분 
> 1. list slicing으로 인해서 시간 초과, 부분합이 S 이상인 수열이 없을 때(min_len이 inf로 남아있을 때) print(0)을 해주지 않았음, 수열의 형태를 유지해야 하는 부분 수열이기 때문에 **sort를 하면 안됨!!**
~~~python
# 부분합
import sys

N, S = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split()))) # nlogn

en = 0
min_len = float('inf')

for st in range(N):
    while en != N - 1 and sum(nums[st:en+1]) < S:
        en += 1
    
    if en == N - 1:
        break
        
    min_len = min(min_len, en - st + 1)

print(min_len)
~~~


> 2. total을 이용하여 st, en을 이동시키고 합을 구한 뒤(sum()이나 list slicing 사용하지 않음) 마지막에 nums[st]를 빼주고 st를 이동시킴
~~~python
# 부분합
import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

en = 0
min_len = float('inf')
total = nums[0]

for st in range(N):
    while en != N - 1 and total < S:
        en += 1
        total += nums[en]

    if total >= S:
        min_len = min(min_len, en - st + 1)

    total -= nums[st]


if min_len == float('inf'):
    print(0)
else:
    print(min_len)
~~~
