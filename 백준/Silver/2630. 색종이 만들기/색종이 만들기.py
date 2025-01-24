# 색종이 만들기
import sys

N = int(sys.stdin.readline())
paper = []
ans = [0, 0]

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def check(sx, sy, size):
    temp = paper[sx][sy]

    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if paper[i][j] != temp:
                return -1

    return temp


def split_paper(sx, sy, size):
    temp = check(sx, sy, size)
    if temp != -1:
        ans[temp] += 1
        return

    size //= 2
    split_paper(sx, sy, size)
    split_paper(sx + size, sy, size)
    split_paper(sx, sy + size, size)
    split_paper(sx + size, sy + size, size)


split_paper(0, 0, N)
print(ans[0])
print(ans[1])