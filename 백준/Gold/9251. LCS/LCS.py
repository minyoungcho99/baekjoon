# LCS
import sys

A, B = sys.stdin.readline().strip(), sys.stdin.readline().strip()

a, b = len(A), len(B)
max_len = -1

LCS = [[0] * (b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

for i in range(1, a+1):
    max_len = max(max_len, LCS[i][b])

print(max_len)