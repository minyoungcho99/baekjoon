# 중앙값 구하기
import sys, heapq

def add(n):
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -n)

    else:
        heapq.heappush(min_heap, n)

    if min_heap and -max_heap[0] > min_heap[0]:
        larger = heapq.heappop(max_heap)
        smaller = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -smaller)
        heapq.heappush(min_heap, -larger)


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    seq = []
    ans = []
    cnt = 0

    min_heap = []
    max_heap = []

    while len(seq) < N:
        seq.extend(map(int, sys.stdin.readline().split()))

    for idx in range(N):
        add(seq[idx])

        if (idx + 1) % 2 != 0:
            ans.append(-max_heap[0])
            cnt += 1

    print(cnt)
    for i in range(0, len(ans), 10):
        print(" ".join(map(str, ans[i:i+10])))