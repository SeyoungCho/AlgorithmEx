def solution(gems):
    answer = [1, 1]
    typeNum = len(set(gems))
    d = {}
    minLen = len(gems)
    startIdx = 1
    setFound = 0
    for i in range(len(gems)):
        d[gems[i]] = i + 1
        if len(d) == typeNum:
            setFound += 1
            if setFound == 1:
                startIdx = min(list(d.values()))
                minName = gems[startIdx - 1]
            if gems[i] == minName:
                startIdx = min(list(d.values()))
                minName = gems[startIdx - 1]
            if i + 1 - startIdx < minLen:
                minLen = i + 1 - startIdx
                answer = [startIdx, i + 1]
    return answer