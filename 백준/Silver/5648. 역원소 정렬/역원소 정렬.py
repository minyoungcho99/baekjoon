# 역원소 정렬
import sys

arr = []
line = list(map(int, sys.stdin.readline().split()))

n = line[0]
for l in line[1:]:
    temp = ""
    l = str(l)
    for i in range(len(l)-1, -1, -1):
        temp += l[i]
    arr.append(int(temp))
    n -= 1

while True:
    line = list(map(int, sys.stdin.readline().split()))
    for l in line:
        l = str(l)
        temp = ""
        for i in range(len(l) - 1, -1, -1):
            temp += l[i]
        arr.append(int(temp))
        n -= 1

    if n == 0:
        break

arr.sort()
for a in arr:
    print(a)