# 치킨 배달
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []

for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))


def find():
    house = []
    chicken = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 0:
                continue
            elif city[i][j] == 1:  # 집
                house.append((i, j))
            else:
                chicken.append((i, j))  # 치킨집

    return house, chicken


def find_min():
    chicken_dist = float('inf')

    index = [i for i in range(len(chicken))]

    for idx in combinations(index, M):
        temp_dist = 0

        for hx, hy in house:
            min_dist = float('inf')

            for k in range(M):
                min_dist = min(min_dist, abs(hx - chicken[idx[k]][0]) + abs(hy - chicken[idx[k]][1]))

            temp_dist += min_dist

        chicken_dist = min(chicken_dist, temp_dist)

    return chicken_dist


house, chicken = find()

if len(chicken) > M:
    print(find_min())

else:
    chicken_dist = 0
    for hx, hy in house:
        temp_dist = float('inf')

        for cx, cy in chicken:
            temp_dist = min(temp_dist, abs(hx - cx) + abs(hy - cy))

        chicken_dist += temp_dist

    print(chicken_dist)