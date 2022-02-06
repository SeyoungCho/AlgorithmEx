import time
from collections import deque
import copy
N = int(input())
# lectures[i] has hours required to complete ith course
lectures = [0] * (N+1)
# indegree list
indegree = [0] * (N+1)
# graph holds the direction info of all the lectures
graph = [[] for _ in range (N+1)]
for i in range(1, N+1):
  line = list(map(int, input().split()))
  lectures[i] = line[0]
  for j in range(1, len(line)-1):
    indegree[i] += 1
    graph[line[j]].append(i)

start_time = time.time()

# result holds the topologically sorted list of lecture numbers
result = copy.deepcopy(lectures)
q = deque()
for i in range(1, N+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  for i in graph[now]:
    indegree[i] -= 1    
    result[i] = max(result[i], result[now] + lectures[i])
    if indegree[i] == 0:
      q.append(i)

for i in range(1, N+1):
  print(result[i], end=' ')
print()
end_time = time.time()
print("time :", end_time - start_time)