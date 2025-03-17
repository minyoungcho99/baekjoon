# 계란으로 계란치기
import sys


def hit(n):
    global ans
    if n == N:
        tmp = 0
        for e in egg:
            if e[0] <= 0:
                tmp += 1

        ans = max(ans, tmp)
        return

    if egg[n][0] <= 0:
        hit(n + 1)
        return

    available = False
    for i in range(N):
        if i == n or egg[i][0] <= 0:
            continue

        egg[n][0] -= egg[i][1]
        egg[i][0] -= egg[n][1]
        available = True
        hit(n+1)
        egg[n][0] += egg[i][1]
        egg[i][0] += egg[n][1]


    if not available:
        hit(n+1)

N = int(sys.stdin.readline())
ans = 0
egg = []

for _ in range(N):
    egg.append(list(map(int, sys.stdin.readline().split())))

hit(0)
print(ans)