"""
다시 풀어봐야 할 문제
<처음에 생각했던 것>
1. 포인터 문제에서 포인터를 뒤로 보낸대도, 정렬되어 있지 않아서 다음에 어떤 값이 올지 몰라서 비효율적으로 탐색할 것 같았음 
-> 각 학급을 sort 해주면 포인터를 뒤로 보낼 수록 값이 커질테니, 최대-최소를 최소화할 때 포인터를 뒤로 보내 효율적인 탐색이 가능

2. 각 학급에 포인터 한 개씩 해서 이동시켜서 비교함, 이때 포인터는 1차원 배열에 담아 추적
-> 1차원 배열보다 heapq에 값과 같이 push해서 최솟값을 빠르게 탐색

3. pointer를 이동시키는 조건이 필요함 ex) while ~~~ and en < N-1: en += 1 
-> 최대-최소의 차이를 작게 하기 위해서는 최솟값을 증가(최솟값을 가진 학급의 포인터를 증가)시켜 최댓값에 가깝게 만드는 방식으로 탐색
"""
# 대표 선수
import sys, heapq

N, M = map(int, sys.stdin.readline().split())
ptr = [0] * N
player = []

for _ in range(N):
    player.append(sorted(list(map(int, sys.stdin.readline().split()))))

pq = []
min_diff = float('inf')
max_val = 0

for idx in range(N):
    heapq.heappush(pq, (player[idx][0], idx, 0))
    max_val = max(max_val, player[idx][0])

while pq:
    min_val, min_idx, min_pointer = heapq.heappop(pq)
    min_diff = min(min_diff, max_val - min_val)

    if min_pointer == M - 1:
        break

    heapq.heappush(pq, (player[min_idx][min_pointer+1], min_idx, min_pointer+1))
    max_val = max(max_val, player[min_idx][min_pointer+1])

print(min_diff)
