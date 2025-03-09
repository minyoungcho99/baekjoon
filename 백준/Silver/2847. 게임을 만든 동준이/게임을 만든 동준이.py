# 게임을 만든 동준이
import sys


def find():
    cnt = 0
    for i in range(N - 1, 0, -1):
        if level[i-1] >= level[i]:
            cnt += (level[i-1] - level[i]) + 1
            level[i-1] -= (level[i-1] - level[i]) + 1

    return cnt


N = int(sys.stdin.readline())

level = []
for _ in range(N):
    level.append(int(sys.stdin.readline()))

print(find())