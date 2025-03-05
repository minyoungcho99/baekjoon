# 회전 초밥
import sys


def count(t):
    cnt = set(t)
    cnt.add(C)

    return len(cnt)


N, D, K, C = map(int, sys.stdin.readline().split())
sushi = []
max_cnt = 0

for _ in range(N):
    sushi.append(int(sys.stdin.readline()))

for st in range(N):
    temp = []
    for i in range(K):
        temp.append(sushi[(st + i) % N])

    max_cnt = max(max_cnt, count(temp))

print(max_cnt)