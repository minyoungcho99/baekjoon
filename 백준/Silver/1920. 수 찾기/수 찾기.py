# 수 찾기
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in range(M):
    target = B[i]
    start = 0
    end = len(A) - 1

    found = False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] < target:
            start = mid + 1
        elif A[mid] > target:
            end = mid - 1
        else:
            print(1)
            found = True
            break

    if not found:
        print(0)