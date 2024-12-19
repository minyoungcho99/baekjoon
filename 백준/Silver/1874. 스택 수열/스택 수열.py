# 스택 수열
import sys

N = int(sys.stdin.readline())
i = 1
possible = True
ops = []
stack = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    while i <= num:
        stack.append(i)
        ops.append('+')
        i += 1 

    if stack[-1] == num:
        stack.pop()
        ops.append('-')
    
    else:
        possible = False

if possible:
    for o in ops:
        print(o)
else:
    print('NO')