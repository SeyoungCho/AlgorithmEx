from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for num in course:
        arr = []
        for order in orders:
            combi = combinations(sorted(order), num)
            arr += combi
        counter = Counter(arr)
        if len(counter) != 0 and max(counter.values()) >= 2:
            answer.extend([''.join(menu) for menu in counter if counter[menu] == max(counter.values())])
    return sorted(answer)