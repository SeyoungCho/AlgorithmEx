def solution(stones, k):
    start = 0
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for num in stones:
            if cnt < k:
                if num <= mid:
                    cnt += 1
                else:
                    cnt = 0
            else:
                break
        if cnt < k: # mid번째가 건널 수 있음
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    return answer