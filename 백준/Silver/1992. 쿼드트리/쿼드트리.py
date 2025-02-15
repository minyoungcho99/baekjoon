# 쿼드트리
import sys

N = int(sys.stdin.readline())
board = []
ans = ""

for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    board.append(list(map(int, line)))


def check(sx, sy, size):
    first = board[sx][sy]
    
    for i in range(sx, sx+size):
        for j in range(sy, sy+size):
            if board[i][j] != first:
                return False, 2

    return True, first


def quadtree(sx, sy, size):
    global ans
    all_same, ctn = check(sx, sy, size)

    if all_same:
        ans += str(ctn)
        return

    size //= 2
    if not all_same:
        ans += "("
        quadtree(sx, sy, size)
        quadtree(sx, sy+size, size)
        quadtree(sx+size, sy, size)
        quadtree(sx+size, sy+size, size)
        ans += ")"


quadtree(0, 0, N)
print(ans)