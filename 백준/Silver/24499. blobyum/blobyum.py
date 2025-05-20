# blobyum
import sys

N, K = map(int, sys.stdin.readline().split())
app = list(map(int, sys.stdin.readline().split()))

res = sum(app[0:K])
temp = sum(app[0:K])

for st in range(N-1):
    temp -= app[st]
    temp += app[(st + K) % N]

    res = max(res, temp)

print(res)