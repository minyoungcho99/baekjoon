# 에라토스테네스의 체
import sys

N, K = map(int, sys.stdin.readline().split())

state = [True] * (N + 1)
state[1] = False
removed = []


for i in range(2, N + 1):
    if not state[i]:
        continue

    removed.append(i)

    if len(removed) == K:
        break

    for j in range(2*i, N + 1, i):
        if not state[j]:
            continue

        state[j] = False
        removed.append(j)

        if len(removed) == K:
            break

    if len(removed) == K:
        break

print(removed[-1])