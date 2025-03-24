# 이차원 배열과 연산
import sys
from collections import defaultdict


def in_range(r, c):
    return 0 <= r < len(A) and 0 <= c < len(A[0])

def r_sort():
    res = []
    for i in range(len(A)):
        temp = []
        a_no_zero = []
        cnt = defaultdict(int)
        for a in A[i]:
            if a != 0:
                a_no_zero.append(a)
                cnt[a] += 1

        a_no_zero = list(set(a_no_zero))
        a_no_zero.sort(key=lambda x: (cnt[x], x))

        for a in a_no_zero:
            temp.append(a)
            temp.append(cnt[a])

        res.append(temp)

    max_len = 0
    for r in res:
        if len(r) > 100:
            r = r[:100]

        max_len = max(max_len, len(r))


    for r in res:
        if len(r) < max_len:
            for _ in range(max_len-len(r)):
                r.append(0)

    return res

def c_sort():
    res = []
    for i in range(len(A[0])):
        temp = []
        a = []
        cnt = defaultdict(int)
        for j in range(len(A)):
            if A[j][i] != 0:
                a.append(A[j][i])
                cnt[A[j][i]] += 1

        a = list(set(a))
        a.sort(key=lambda x: (cnt[x], x))

        for ele in a:
            temp.append(ele)
            temp.append(cnt[ele])

        res.append(temp)

    max_len = 0
    for r in res:
        if len(r) > 100:
            r = r[:100]

        max_len = max(max_len, len(r))

    final = [[0] * len(res) for _ in range(max_len)]

    for i in range(len(res)):
        for j in range(len(res[i])):
            final[j][i] = res[i][j]

    return final

R, C, K = map(int, sys.stdin.readline().split())
A = []

for _ in range(3):
    A.append(list(map(int, sys.stdin.readline().split())))

time = 0

while time <= 100:
    # print()
    # for a in A:
    #     print(a)
    if in_range(R-1, C-1):
        if A[R-1][C-1] == K:
            print(time)
            break

    if len(A) >= len(A[0]):
        A = r_sort()

    else:
        A = c_sort()

    time += 1

if time > 100:
    print(-1)