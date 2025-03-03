# 문자열 찾기
import sys

st = sys.stdin.readline().rstrip()
k = 0
io = 0

for i in range(len(st)-2):
    if st[i:i+3] == "KOI":
        k += 1
    elif st[i:i+3] == "IOI":
        io += 1

print(k)
print(io)
