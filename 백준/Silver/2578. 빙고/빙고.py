# 빙고
import sys

def check():
    cnt = 0
    for i in range(5):
        if len(set(board[i])) == 1:
            cnt += 1

    temp = list(zip(*board))
    for i in range(5):
        if len(set(temp[i])) == 1:
            cnt += 1

    temp = [board[i][i] for i in range(5)]
    if len(set(temp)) == 1:
        cnt += 1

    temp = [board[i][4-i] for i in range(5)]
    if len(set(temp)) == 1:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False

board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

called = []
for _ in range(5):
    called.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
for i in range(5):
    for j in range(5):
        is_found = False

        for bi in range(5):
            for bj in range(5):
                if called[i][j] == board[bi][bj]:
                    board[bi][bj] = 27
                    is_found = True
                    break

            if is_found:
                break

        chk = check()

        if chk:
            print(cnt)
            break
        cnt += 1

    if chk:
        break