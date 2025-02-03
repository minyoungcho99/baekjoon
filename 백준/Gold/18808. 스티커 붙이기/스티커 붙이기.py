# 스티커 붙이기
import sys

N, M, K = map(int, sys.stdin.readline().split())

notebook = [[0] * M for _ in range(N)]
stickers = []

for _ in range(K):
    sticker = []
    R, C = map(int, sys.stdin.readline().split())

    for _ in range(R):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    stickers.append([(R, C), sticker, True])


def in_range(sx, sy, R, C):
    return 0 <= sx + R <= N and 0 <= sy + C <= M


def match(num):
    R, C = stickers[num][0]
    s = stickers[num][1]

    for sx in range(N):
        for sy in range(M):
            if in_range(sx, sy, R, C):
                is_matched = True

                for x in range(R):
                    for y in range(C):
                        if s[x][y] == 1:
                            if notebook[sx+x][sy+y] == 1:
                                is_matched = False
                                break

                    if not is_matched:
                        break

            else:
                break

            if is_matched:
                return sx, sy

    return -1, -1


def rotate(num):
    R, C = stickers[num][0]
    s = stickers[num][1]
    is_able = stickers[num][2]

    rotated = [[0] * R for _ in range(C)]

    # print(num, R, C)
    # print("before rotation")
    # for st in s:
    #     print(st)

    for i in range(C):
        for j in range(R):
            rotated[i][j] = s[R-1-j][i]

    # print("after rotation")
    # for r in rotated:
    #     print(r)

    stickers[num] = [(C, R), rotated, is_able]


def mark(sx, sy, num):
    R, C = stickers[num][0]
    s = stickers[num][1]

    # print("here fr")
    # for st in s:
    #     print(st)

    for i in range(R):
        for j in range(C):
            if s[i][j] == 1:
                notebook[sx+i][sy+j] = 1

    stickers[num][2] = True


def count():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if notebook[i][j] == 1:
                cnt += 1

    return cnt


for i in range(K):
    if stickers[i][2]:
        tx, ty = match(i)

        cnt = 0
        while True:
            if (tx, ty) != (-1, -1):
                break

            if cnt > 3:
                stickers[i][2] = False
                break

            rotate(i)
            tx, ty = match(i)
            cnt += 1

            # print('here!!')
            # print(tx, ty)

        if (tx, ty) != (-1, -1) and stickers[i][2]:
            mark(tx, ty, i)

    # print("notebook:")
    # for n in notebook:
    #     print(n)

print(count())