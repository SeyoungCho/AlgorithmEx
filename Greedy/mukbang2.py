import heapq

def solution(food_times, k):
	answer = -1
	food_cnt = len(food_times)
	q = []
	for i in range(food_cnt):
		heapq.heappush(q, (food_times[i], i+1))
	prev = 0

	while q:
		diff = (q[0][0]-prev) * food_cnt
		if k >= diff:
			food_cnt -= 1
			k -= diff
			prev, _ = heapq.heappop(q)
		else:
			idx = k % food_cnt
			q.sort(key = lambda x: x[1])
			answer = q[idx][1]
			break
	return answer
			
print(solution([2,2,3], 6))			