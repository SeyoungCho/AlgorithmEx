import time
import sys
from collections import deque
N, K = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
start_time = time.time() 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = [[] for _ in range(K+1)]

#save the location of each viruses
for i in range(N):
  for j in range(N):
    #if there's a virus	
    if graph[i][j] != 0:
      #store the location of the virus
      virus[graph[i][j]].append((i, j))

#queue used for bfs
q = deque([])
for i in range(1, len(virus)):
  for x, y in virus[i]:
    #append into the queue [virus no, x, y, spread time]
    q.append([i, x, y, 1])
while q:
  vir_no, x, y, t = q.popleft()
  #if it passes the last second
  if t > S:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < N and ny >= 0 and ny < N:
      if graph[nx][ny] == 0:
        graph[nx][ny] = vir_no
        q.append([vir_no, nx, ny, t+1])

print(graph[X-1][Y-1])
end_time = time.time() 
print("time :",end_time - start_time)