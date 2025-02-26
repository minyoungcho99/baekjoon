# 빈도 정렬
import sys, heapq
from collections import defaultdict

N, C = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = defaultdict(int)
q = []
result = []

for i in range(len(arr)):
    cnt[arr[i]] += 1

for a in arr:
    heapq.heappush(q, (-cnt[a], arr.index(a), a))

while q:
    result.append(heapq.heappop(q)[2])

print(" ".join(map(str, result)))