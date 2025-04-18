# 종이 자르기
import sys

n, m = map(int, sys.stdin.readline().split())
w = [0, n]
h = [0, m]

l = int(sys.stdin.readline())

for _ in range(l):
    mode, num = map(int, sys.stdin.readline().split())

    if mode == 0: # 가로
        h.append(num)

    else:
        w.append(num)

h.sort()
w.sort()

tw = []
for i in range(1, len(w)):
    tw.append(w[i]-w[i-1])

th = []
for i in range(1, len(h)):
    th.append(h[i] - h[i-1])

print(max(tw)*max(th))