import time
from itertools import combinations

N, M = map(int, input().split())
city = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(1, N+1):
  city[i] = [0] + list(map(int, input().split())) + [0]
 
start_time = time.time() 

home = []
chicken = []
#distance[i]: chicken distance of ith home

for i in range(1, N+1):
  for j in range(1, N+1):
    #home
    if city[i][j] == 1:
      home.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))
    else:
      pass
distance = [99999] * len(home)
#list of possible combinations of M chicken places
testCase = list(combinations(range(len(chicken)), M))
#get chicken distance of all homes
answer = sum(distance)
for case in testCase:
  distance = [99999] * len(home)
  for i in range(len(home)):
    hx, hy = home[i]
    for j in case:
      cx, cy = chicken[j]
      distance[i] = min(distance[i], abs(hx-cx) + abs(hy-cy))
  answer = min(answer, sum(distance))

print(answer)
end_time = time.time() 
print("time :",end_time - start_time)