# 공통 부분 문자열
import sys

max_str = 0
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

a, b = len(A), len(B)

LCS = [[0] * (a+1) for _ in range(b+1)]

for i in range(1, b+1):
    for j in range(1, a+1):
        if B[i-1] == A[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
            max_str = max(max_str, LCS[i][j])

print(max_str)