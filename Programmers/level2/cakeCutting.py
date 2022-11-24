def solution(topping):
    answer = 0
    b = dict()
    for t in topping:
        if t in b:
            b[t] += 1
        else:
            b[t] = 1
    c = set([])
    for t in topping:
        c.add(t)
        b[t] -= 1
        if b[t] == 0:
            del b[t]
        if len(c) == len(b.keys()):
            answer += 1
    return answer