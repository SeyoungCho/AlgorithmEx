import time
INF = int(1e9) #infinity
N,M = map(int, input().split())
graph = [[INF] * (N+1) for i in range(N+1)]
for _ in range(M):
  _from, to = map(int, input().split())
  graph[_from][to] = 1
  graph[to][_from] = 1
X, K = map(int, input().split())
start_time = time.time()
#assign 0 for paths to themselves
for i in range(1, N+1):
  graph[i][i] = 0
#floyd_warshall for all the cities
for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      continue
    for k in range(1, N+1):
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
print(graph[1][K] + graph[K][X])
end_time = time.time()
print("time :", end_time-start_time)
