# 뒤집기
import sys

stri = list(map(int, sys.stdin.readline().rstrip()))

before = 2
cnt = 0

for i in range(len(stri)):
    if stri[i] != before:
        cnt += 1
        before = stri[i]

print(cnt // 2)