# 가운데를 말해요
import sys, heapq

min_heap = []
max_heap = []


def add(num):
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)

    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        larger = heapq.heappop(max_heap)
        smaller = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -smaller)
        heapq.heappush(min_heap, -larger)


N = int(sys.stdin.readline())

for _ in range(N):
    A = int(sys.stdin.readline())
    add(A)
    print(-max_heap[0])