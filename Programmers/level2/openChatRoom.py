def build_dict(users, record):
    for log in record[::-1]:
        fLog = log.split()
        if fLog[0] != "Leave":
            if users.get(fLog[1]) == None:
                users[fLog[1]] = fLog[2]
                
def solution(record):
    answer = []
    users = {}
    behaviors = {
        "Enter" : "들어왔습니다.",
        "Leave" : "나갔습니다."
    }
    build_dict(users, record)
    for log in record:
        fLog = log.split()
        if fLog[0] != "Change":
            answer.append(users[fLog[1]] + '님이 ' + behaviors[fLog[0]])
    return answer