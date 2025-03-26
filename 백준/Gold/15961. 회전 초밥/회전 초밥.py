# 회전 초밥
import sys

def sliding_window():
    max_num = 0
    unique_cnt = 0
    cnt = [0] * d

    for i in range(k):
        if cnt[sushi[i]-1] == 0:
            unique_cnt += 1
        cnt[sushi[i]-1] += 1

    if cnt[c-1] == 0:
        unique_cnt += 1
    cnt[c-1] += 1

    for st in range(N):
        max_num = max(max_num, unique_cnt)

        cnt[sushi[st]-1] -= 1
        if cnt[sushi[st]-1] == 0:
            unique_cnt -= 1

        if cnt[sushi[(st + k) % N]-1] == 0:
            unique_cnt += 1
        cnt[sushi[(st + k) % N]-1] += 1

    return max_num

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = []

for _ in range(N):
    sushi.append(int(sys.stdin.readline()))

print(sliding_window())