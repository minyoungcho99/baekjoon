from bisect import bisect_left, bisect_right

def binary_search(arr, x, c):
    if c == 0:
        return arr[:bisect_left(nums, x)]

    else:
        return arr[bisect_right(nums, x):]
      
n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for _ in range(k):
    x, c = map(int, input().split())
    nums = binary_search(nums, x, c)

print(len(nums))
