import sys

num = list(map(int, sys.stdin.readline().split()))
K = num[0]
num = num[1:]


def recursion(temp, idx):
    if len(temp) == 6:
        print(" ".join(map(str, temp)))
        return

    for i in range(idx, K):
        recursion(temp + [num[i]], i+1)


recursion([], 0)
