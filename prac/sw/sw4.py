import sys
from collections import Counter

T = int(sys.stdin.readline())

for _ in range(T):
    N, R = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    temp = lst[-R:] + lst[:R+1]
    possible = True

    for i in range(R+1, N+R):
        cnt = Counter(temp)
        for c in cnt:
            if cnt[c] >= 3:
                possible = False
                break

        temp = temp[1:]
        temp.append(lst[i % N])

        if not possible:
            break

    if possible:
        print(f"#{_+1} YES")

    else:
        print(f"#{_+1} NO")
