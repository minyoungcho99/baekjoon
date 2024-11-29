# 로프
import sys

N = int(sys.stdin.readline())
l = []

for _ in range(N):
    l.append(int(sys.stdin.readline().strip()))
    
l.sort()

max_weight = 0
for i in range(1, N + 1):
    max_weight = max(max_weight, l[N-i] * i)

print(max_weight)