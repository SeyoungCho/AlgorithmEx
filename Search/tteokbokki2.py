#Binary Search Solution
import time
N, M = map(int, input().split())
tteoks = list(map(int, input().split()))
start_time = time.time()

start = 0
end = max(tteoks)
result = 0
while start <= end:  
  mid = (start + end) // 2
  output = [i-mid for i in tteoks if i > mid]
  if sum(output) < M:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
    
print(result)
end_time = time.time() 
print("time :", end_time - start_time)