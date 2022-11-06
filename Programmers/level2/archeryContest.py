def getBestCase(ans, tr, n):
    for i in range(n-1, -1, -1):
        if tr[i] > ans[i]:
            return True
        elif ans[i] > tr[i]:
            return False
    return False

def dfs(answer, info, n, max, trial, i):
    if n == 0 or i == 11: #다 쏜것
        ryan = 0
        apeach = 0
        for i in range(11):
            if trial[i] > info[i]:
                ryan += 10 - i
            else:
                if info[i] != 0:
                    apeach += 10 - i
        diff = ryan - apeach
        if diff > max[0]:
            max[0] = diff
            if n > 0:
                trial[10] = n
            for i in range(len(trial)):
                answer[i] = trial[i]
        elif diff == max[0]:
            if n > 0:
                trial[10] = n
            if getBestCase(answer, trial, 11) == 1:
                max[0] = diff
                for i in range(len(trial)):
                    answer[i] = trial[i]
        trial[10] = 0
        return
    else:
        if n >= info[i] + 1:
            trial[i] = info[i] + 1
            dfs(answer, info, n-(info[i]+1), max, trial, i+1)
            trial[i] = 0
        dfs(answer, info, n, max, trial, i+1)
    
def solution(n, info):
    answer = [0] * 11
    trial = [0] * 11
    max = [0]
    dfs(answer, info, n, max, trial, 0)
    if max[0] == 0:
        return [-1]
    return answer