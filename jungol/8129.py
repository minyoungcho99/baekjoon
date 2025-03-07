import sys

N, K = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))
num = [i for i in range(1, N + 1)]
ans = []


def combination(temp, idx):
    if len(temp) == K:
        ans.append(temp)
        return

    for i in range(idx, N):
        combination(temp + [num[i]], i + 1)


combination([], 0)

try:
    print(ans.index(target)+1)
except:
    print("None")
