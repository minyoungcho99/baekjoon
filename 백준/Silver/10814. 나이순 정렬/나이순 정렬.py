# 나이순 정렬
import sys

N = int(sys.stdin.readline())
info = []

for _ in range(N):
    age, name = tuple(sys.stdin.readline().split())
    age = int(age)
    info.append((age, name))

for age, name in sorted(info, key=lambda x: x[0]):
    print(age, name)