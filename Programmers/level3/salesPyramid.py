import math
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    enroll_list = {name : i for i, name in enumerate(enroll)}
    for i, name in enumerate(enroll):
        enroll_list[name] = i
    for (name, amt) in zip(seller, amount):
        distribution = amt * 10
        profit = amt * 90
        while True:
            idx = enroll_list[name]
            answer[idx] += profit
            if referral[idx] == '-' or profit / 10 == 0:
                break
            #다음 분배를 위한 변수 업데이트
            name = referral[idx]
            profit = distribution - math.floor(distribution*0.1)
            distribution = math.floor(distribution * 0.1)
    return answer