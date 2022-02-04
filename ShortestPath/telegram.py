import time
import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))
  
start_time=time.time()
distance = [INF] * (N+1)

#dijkstra method using priority queue
def dijkstra(graph, start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (distance[start], start))
  while q:  #until the queue is empty
    dist, now = heapq.heappop(q)
    if distance[now] < dist:  #skip for the nodes that are already confirmed
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
dijkstra(graph, C)
#get maximum cost and number of cities we can reach out to
max_time = 0
city_cnt = 0
for i in range(1, N+1):
  if distance[i] != INF:
    if i != C:
      city_cnt += 1
    if distance[i] > max_time:
      max_time = distance[i]

print(city_cnt, max_time)

end_time=time.time()
print("time :",end_time-start_time)
