def solution(n,a,b):
    answer = 1
    while abs(a - b) > 1 or max(a, b) % 2 != 0:
        answer += 1
        if a % 2 == 1:
            a = (a + 1) // 2
        else:
            a = a // 2
        if b % 2 == 1:
            b = (b + 1) // 2
        else:
            b = b // 2
    return answer