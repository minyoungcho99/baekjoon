def solution(n, info):
    def count(info, ans):
        apeach, lion = 0, 0
        for i in range(11):
            if info[i] == 0 and ans[i] == 0:
                continue
            if info[i] >= ans[i]:
                apeach += 10 - i
            else:
                lion += 10 - i
        return apeach, lion

    def dfs(depth, idx, ans, remain):
        nonlocal max_diff, max_arr

        if depth == n or idx == 11:
            if depth < n:
                ans[10] += (n - depth)
            ap, li = count(info, ans)
            diff = li - ap
            if diff > 0:
                if diff > max_diff or (diff == max_diff and ans[::-1] > max_arr[::-1]):
                    max_diff = diff
                    max_arr = ans[:]
            if depth < n:
                ans[10] -= (n - depth)
            return

        need = info[idx] + 1
        if remain >= need:
            ans[idx] = need
            dfs(depth + need, idx + 1, ans, remain - need)
            ans[idx] = 0

        # 현재 점수 포기
        dfs(depth, idx + 1, ans, remain)

    max_diff = -1
    max_arr = [-1]

    dfs(0, 0, [0] * 11, n)
    return max_arr