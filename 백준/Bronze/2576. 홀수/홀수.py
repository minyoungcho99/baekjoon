# 홀수
import sys

odd = []
for _ in range(7):
    x = int(sys.stdin.readline())

    if x % 2 != 0:
        odd.append(x)

if len(odd) == 0:
    print(-1)

else:
    print(sum(odd))
    print(min(odd))