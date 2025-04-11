# 선택 정렬
# 가장 작은 값을 골라서 앞으로 보내는 정렬
# 시간복잡도: O(n^2)
# in-place, not stable

arr = [0,7,8,3,4]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
