"""
틀린 부분:
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

대칭을 안시켜줌.. 걍 문제를 안읽음.. 
"""

# 테트로미노
import sys
from copy import deepcopy


def rotate(t):
    n, m = len(t), len(t[0])
    temp_90 = [[0] * n for _ in range(m)]
    temp_180 = [[0] * m for _ in range(n)]
    temp_270 = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            temp_90[j][n - i - 1] = t[i][j]

    for i in range(n):
        for j in range(m):
            temp_180[n - i - 1][m - j - 1] = t[i][j]

    for i in range(n):
        for j in range(m):
            temp_270[m - j - 1][i] = t[i][j]

    return temp_90, temp_180, temp_270


def symme(t):
    sym = []

    for i in range(len(t)):
        sym.append(t[i][::-1])

    return sym


def find_max(t, t1, t2, t3):
    max_score = float('-inf')

    a, b = len(t), len(t[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if t[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    sym = symme(t)
    a, b = len(t), len(t[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if sym[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    a, b = len(t1), len(t1[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if t1[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    sym_90 = symme(t1)
    a, b = len(t1), len(t1[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if sym_90[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    a, b = len(t2), len(t2[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if t2[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    sym_180 = symme(t2)
    a, b = len(t2), len(t2[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if sym_180[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    a, b = len(t3), len(t3[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if t3[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    sym_270 = symme(t3)
    a, b = len(t3), len(t3[0])
    for sx in range(N - a + 1):
        for sy in range(M - b + 1):
            temp = 0
            for i in range(a):
                for j in range(b):
                    if sym_270[i][j] == 1:
                        temp += board[sx + i][sy + j]

            max_score = max(max_score, temp)

    return max_score


te = [[[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
      [[1, 1, 1], [0, 1, 0]]]

max_score = float('-inf')

N, M = map(int, sys.stdin.readline().split())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for t in te:
    temp = deepcopy(t)
    rotated_90, rotated_180, rotated_270 = rotate(temp)
    temp_max = find_max(temp, rotated_90, rotated_180, rotated_270)

    max_score = max(max_score, temp_max)

print(max_score)
