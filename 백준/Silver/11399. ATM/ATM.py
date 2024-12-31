N = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0

for t in times:
    result += (N * t)
    N -= 1

print(result)