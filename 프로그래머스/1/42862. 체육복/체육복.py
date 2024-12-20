def solution(n, lost, reserve):
    for l in lost[:]:
        if l in reserve[:]:
            lost.remove(l)
            reserve.remove(l)

    temp = len(lost)

    for l in sorted(lost):
        if l - 1 in reserve:
            reserve.remove(l - 1)
            temp -= 1
            continue

        elif l + 1 in reserve:
            reserve.remove(l + 1)
            temp -= 1
            continue

    return n - temp


print(solution(5, [2, 3], [3, 4]))