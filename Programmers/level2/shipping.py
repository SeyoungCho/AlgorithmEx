# update 
def update(remain, last_idx, total, cap):
    for i in range(last_idx, -1, -1):
        if remain[i] == 0:
            continue
        if cap == 0:
            break
        if cap >= remain[i]:
            total -= remain[i]
            cap -= remain[i]
            remain[i] = 0
        else:
            total -= cap
            remain[i] -= cap
            cap = 0
            break
    return total

def solution(cap, n, deliveries, pickups):
    answer = 0
    last_idx = len(deliveries) - 1
    total_d = sum(deliveries)
    total_p = sum(pickups)
    while total_d or total_p:
        while deliveries[last_idx] == 0 and pickups[last_idx] == 0:
            last_idx -= 1
        if total_d:
            total_d = update(deliveries, last_idx, total_d, cap)
        if total_p:
            total_p = update(pickups, last_idx, total_p, cap)
        answer += (last_idx + 1) * 2        
    return answer