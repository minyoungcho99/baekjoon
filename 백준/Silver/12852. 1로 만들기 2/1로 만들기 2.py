# 1로 만들기 2
import sys

N = int(sys.stdin.readline())
D = [0] * (N + 1)
pre = [0] * (N + 1)

D[1] = 0

for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    pre[i] = i - 1

    if i % 2 == 0 and D[i] > D[i // 2] + 1:
        D[i] = D[i // 2] + 1
        pre[i] = i // 2

    if i % 3 == 0 and D[i] > D[i // 3] + 1:
        D[i] = D[i // 3] + 1
        pre[i] = i // 3

print(D[N])

j = N

while True:
    print(j, end=' ')

    if j == 1:
        break

    j = pre[j]
