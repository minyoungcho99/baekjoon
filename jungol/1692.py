import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
str_b = str(B)

ans = [0] * 3
for i in range(len(str_b)):
    ans[i] = A * int(str_b[i])

print(ans[2])
print(ans[1])
print(ans[0])
print(A*B)
