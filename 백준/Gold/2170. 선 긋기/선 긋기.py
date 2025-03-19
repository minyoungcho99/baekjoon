"""
틀린 부분
1. 일단 last = 0으로 놓고 0번부터 순회함 0번부터 순회하려면 last = -1000000000로 놔야함 안그러면 음수 구간은 탐색을 안하게 됨
last를 0번 인덱스의 en으로 놓고 1번부터 탐색하면서 해결!

2. elif 의 경우만 생각했었음, st < last < en 처럼 중간에 낄 때는 en - last로 더해진 부분만 더해줘야 함
if st < last < en:
    cnt += en - last
    last = en
좀 바로 포기하지 말고 꼼꼼하게 생각해보자^^..

"""
# 선 긋기
import sys


def count():
    last = line[0][1]
    cnt = line[0][1] - line[0][0]

    for st, en in line[1:]:
        if st < last < en:
            cnt += en - last
            last = en

        elif st >= last:
            cnt += abs(en - st)
            last = en

    return cnt


N = int(sys.stdin.readline())
line = []

for _ in range(N):
    line.append(tuple(map(int, sys.stdin.readline().split())))

line.sort()
print(count())
