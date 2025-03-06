import sys

N = int(sys.stdin.readline())
if 1 <= N <= 50 and N % 2 == 1:
    tri = [[] for _ in range(N)]
    time = N * 2 - 1
    tmp = 0

    while time > 0:
        for _ in range(tmp):
            tri[tmp].append(' ')

        for _ in range(time):
            tri[tmp].append(tmp)

        tmp += 1
        time -= 2

    for t in tri:
        print(" ".join(map(str, t)))
else:
    print("INPUT ERROR!")
