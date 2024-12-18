# 소수 구하기
import sys

M, N = map(int, sys.stdin.readline().split())

state = [True] * (N + 1)
state[1] = False

for num in range(2, N + 1):
    if not state[num]:
        continue

    for i in range(2 * num, N + 1, num):
        state[i] = False

for num in range(M, N + 1):
    if state[num]:
        print(num)