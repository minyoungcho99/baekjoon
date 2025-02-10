# 블로그
import sys

N, X = map(int, sys.stdin.readline().split())
today = list(map(int, sys.stdin.readline().split()))

temp = 0
for i in range(X):
    temp += today[i]

max_today = temp

for pt in range(1, N - X + 1):
    temp -= today[pt-1]
    temp += today[pt+X-1]

    max_today = max(max_today, temp)

if max_today == 0:
    print("SAD")

else:
    ans = 0
    temp = 0
    for i in range(X):
        temp += today[i]

    if temp == max_today:
        ans += 1

    for pt in range(1, N - X + 1):
        temp -= today[pt - 1]
        temp += today[pt + X - 1]

        if temp == max_today:
            ans += 1

    print(max_today)
    print(ans)