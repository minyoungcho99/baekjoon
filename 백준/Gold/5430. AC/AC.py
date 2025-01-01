# AC 
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    is_error = False
    is_reversed = False

    ops = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    l = sys.stdin.readline().strip()
    l = l[1:len(l)-1].split(',')

    if n == 0:
        l = []

    q = deque(l)

    for o in ops:
        if o == 'R':
            is_reversed = not is_reversed
        else:
            if q:
                if is_reversed:
                    q.pop()
                else:
                    q.popleft()
            else:
                print("error")
                is_error = True
                break

    if not is_error:
        result = list(q)
        if is_reversed:
            result.reverse()
        string = ",".join(result)
        print(f"[{string}]")