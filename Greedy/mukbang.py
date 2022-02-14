import time
import heapq
from bisect import bisect_left
#number of food
N = int(input())
data = list(map(int, input().split()))
#second when the network goes down
K = int(input())
start_time = time.time()

#food times array
food_times = []
#the result
result = -1
# push all the food info into the priority queue
for i in range(len(data)):
  heapq.heappush(food_times, (data[i], i+1))
# find out which food runs out the latest before K seconds
#n is the number of remaining food 
n = N
#amount of food that's previously been finished
previous = 0
while food_times:
  t = (food_times[0][0] - previous) * n
  #network still on
  if K > t:
    K -= t
    previous, _ = heapq.heappop(food_times)
    n -= 1
  #network went down before finishing this round
  else:
    food_times.sort(key=lambda x : x[1])
    start_idx = K % n
    result = food_times[start_idx][1]
    break


print(result)    

end_time = time.time()
print("time :", end_time - start_time)