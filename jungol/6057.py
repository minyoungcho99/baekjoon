import sys
from collections import deque, defaultdict

P, N = map(int, sys.stdin.readline().split())
profit = 0
pizza = defaultdict(deque)

for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 0: # 피자 제작
        pizza[cmd[1]].append(cmd[2])

    else:
        if len(pizza[cmd[1]]) > 0:
            p, v = pizza[cmd[1]].popleft()
            profit += v

print(profit)
