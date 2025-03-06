import sys

N = int(sys.stdin.readline())
if 1 <= N <= 50 and N % 2 == 1:
    tri = [[] for _ in range(N)]

    tmp = 0
    while tmp != N // 2 + 1:
        for i in range(tmp, N-tmp):
            tri[i].append(tmp+1)

        tmp += 1

    for t in tri:
        print(" ".join(map(str, t)))

else:
    print("INPUT ERROR!")
