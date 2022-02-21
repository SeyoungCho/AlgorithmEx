import time
from collections import deque
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  source, dest = map(int, input().split())
  graph[source].append(dest)
start_time = time.time()
INF = int(1e9)
distance = [0] * (N+1)
visited = [False] * (N+1)
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        distance[i] = distance[v] + 1
        queue.append(i) 

bfs(graph, X, visited)

city_list = []
for i in range(1, len(distance)):
  if distance[i] == K:
    city_list.append(i)
city_list.sort()
if city_list:
  for i in range(len(city_list)):
    print(city_list[i])
else:
  print(-1)

  
end_time = time.time() 
print("time :",end_time - start_time)