# 2048 (Easy)
import sys

def move(bor):
    for i in range(N):
        prev = 0
        temp = []
        for b in bor[i]:
            if b > 0: # 빈 칸이 아니라면
                if prev == b:
                    temp.append(prev*2)
                    prev = 0

                else:
                    if prev == 0:
                        prev = b

                    else:
                        temp.append(prev)
                        prev = b

        if prev != 0:
            temp.append(prev)

        if len(temp) < N:
            for _ in range(N-len(temp)):
                temp.append(0)

        bor[i] = temp

def dfs(depth, bor):
    global ans
    if depth == 5:
        ans = max(ans, max(map(max, bor)))
        return

    # 좌 -> 우
    temp = [b[:] for b in bor]
    move(temp)
    dfs(depth+1, temp)

    # 우 -> 좌
    temp = [b[::-1] for b in bor]
    move(temp)
    dfs(depth + 1, temp)

    # 위 -> 아래
    tbor = list(map(list, zip(*bor)))
    temp = [b[:] for b in tbor]
    move(temp)
    dfs(depth + 1, temp)

    # 아래 -> 위
    tbor = list(map(list, zip(*bor)))
    temp = [b[::-1] for b in tbor]
    move(temp)
    dfs(depth + 1, temp)

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

ans = 0
dfs(0, board)
print(ans)