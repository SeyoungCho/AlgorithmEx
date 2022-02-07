import time
# number of food
N = int(input())
food_times = list(map(int, input().split()))
#second when the network goes down
K = int(input())
finished = 0
start_time = time.time()

#count the no.of finished food after K seconds
for i in range(len(food_times)):
  if K <= food_times[i] * (N-1) + i:
    finished += 1
    food_times[i] = 0

#Determine which food number to resume with
if finished == N:
  print(-1)
else:
  result = (K + finished) % N
  print(result)
end_time = time.time()
print("time :", end_time - start_time)