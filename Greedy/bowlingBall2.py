import time
N, M = map(int, input().split())
balls = list(map(int, input().split()))
start_time = time.time()

result = 0
#count[i]: has number of balls with weight i 
count = [0] * (M+1)
for i in range(1,M+1):
  count[i] = balls.count(i)

#loop through the count array and add (no. of selectables * no.of selected) to the result
for i in range(1, M+1):
  N -= count[i]
  result += count[i] * N
print(result)
end_time = time.time()
print("time :",end_time - start_time)