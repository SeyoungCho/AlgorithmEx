import datetime as dt
import collections 
import math

def checkIn(num, time, answer):
    if num in answer.keys():
        answer[num][0] = time
    else:
        answer[num] = [time, 0]

def checkOut(num, time, answer):
    inTime, total_t = answer[num]
    y = 2022
    m = 11
    d = 6
    in_h = int(inTime.split(":")[0])
    in_m = int(inTime.split(":")[1])
    h = int(time.split(":")[0])
    min = int(time.split(":")[1])
    t_diff = int((dt.datetime(y, m, d, h, min) - dt.datetime(y, m, d, in_h, in_m)).total_seconds() / 60)
    answer[num] = ["23:59", t_diff + total_t]

def getFee(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
def solution(fees, records):
    answer = dict()
    y = 2022
    m = 11
    d = 6
    for rec in records:
        time, num, inOrOut = rec.split()
        if inOrOut == "IN":
            checkIn(num, time, answer)
        else:
            checkOut(num, time, answer)
    for key, val in answer.items():
        if val[0] != "23:59":
            in_h = int(val[0].split(":")[0])
            in_m = int(val[0].split(":")[1])
            val[1] += int((dt.datetime(2022, 11, 6, 23, 59) - dt.datetime(2022, 11, 6, in_h, in_m)).total_seconds() / 60)
    od = collections.OrderedDict(sorted(answer.items()))
    return [getFee(info[1], fees) for num, info in od.items()]