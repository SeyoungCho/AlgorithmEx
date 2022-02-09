import time
import heapq
#number of food
N = int(input())
data = list(map(int, input().split()))
#second when the network goes down
K = int(input())
start_time = time.time()

#food times array
food_times = []
#number of finished food
finished = 0
# push all the food info into the priority queue
for i in range(len(data)):
  heapq.heappush(food_times, (data[i], i))

result = 0
print(result)    


#pop from the queue until sum is less than K
end_time = time.time()
print("time :", end_time - start_time)