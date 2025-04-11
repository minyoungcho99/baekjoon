# 버블 정렬
# 인접한 두 원소를 비교하면서 정렬
# 시간복잡도: O(n^2)
# in-place, stable

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
