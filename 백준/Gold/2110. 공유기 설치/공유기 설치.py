# 공유기 설치
import sys


def count(dist):
    temp = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] - temp >= dist:
            cnt += 1
            temp = house[i]

    return cnt


def binary_search(st, en):
    last = 0

    while st <= en:
        mid = (st + en) // 2
        if count(mid) >= C:
            st = mid + 1
            last = mid

        else:
            en = mid - 1

    return last

N, C = map(int, sys.stdin.readline().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
first = house[0]
last = house[N-1]
print(binary_search(0, last-first))