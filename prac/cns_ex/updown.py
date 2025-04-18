from bisect import bisect_left, bisect_right

# def binary_search(arr, x, c):
#     st, en = 0, len(arr) - 1
#     last = -1  # 없을 경우를 고려해서 -1

#     while st <= en:
#         mid = (st + en) // 2

#         if arr[mid] <= x:
#             last = mid
#             st = mid + 1
#         else:
#             en = mid - 1

#     if c == 0:  # 다운이라면
#         return arr[:last+1] 

#     else:  # 업이라면
#         return arr[last+1:]
        
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
