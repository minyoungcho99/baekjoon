n, k = map(int, input().split())
nums = set(map(int, input().split()))
orig = set(x for x in range(1, n+1))

print(sum(orig-nums))
