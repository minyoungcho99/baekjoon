# 종이의 개수
import sys
import math

N = int(sys.stdin.readline())
paper = []

neg = 0
zero = 0
pos = 0

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))


def check(sx, sy, d):
    temp = paper[sx][sy]
    for i in range(sx, sx + 3**d):
        for j in range(sy, sy+ 3**d):
            if paper[i][j] != temp:
                return 2

    return temp


def split_paper(sx, sy, d):
    global neg, zero, pos

    if check(sx, sy, d) != 2:
        if check(sx, sy, d) == -1:
            neg += 1

        elif check(sx, sy, d) == 0:
            zero += 1

        else:
            pos += 1
        return

    # recursive call
    split_paper(sx, sy, d - 1)
    split_paper(sx + 3**(d - 1), sy, d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy, d - 1)

    split_paper(sx, sy + 3**(d - 1), d - 1)
    split_paper(sx + 3**(d - 1), sy + 3**(d - 1), d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy + 3**(d - 1), d - 1)

    split_paper(sx, sy + 2 * 3**(d - 1), d - 1)
    split_paper(sx + 3**(d - 1), sy + 2 * 3**(d - 1), d - 1)
    split_paper(sx + 2 * 3**(d - 1), sy + 2 * 3**(d - 1), d - 1)


split_paper(0, 0, int(round(math.log(N, 3)))) # call
print(neg)
print(zero)
print(pos)