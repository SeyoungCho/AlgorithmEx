def solution(n):
    ans = 0
    while n > 0:
        d, m = divmod(n, 2)
        if m == 1:
            ans += 1
        n = d
    return ans