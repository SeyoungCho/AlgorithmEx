from collections import Counter
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

def solution2(topping):
    answer = 0
    b = Counter(topping)
    c = set([])
    for i in topping[:len(topping)-1]:
        c.add(i)
        if i in b:
            b[i] -= 1
            if b[i] == 0:
                del b[i]
        if len(c) == len(b):
            answer += 1
    return answer