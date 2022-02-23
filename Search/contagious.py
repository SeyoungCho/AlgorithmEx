import time
import sys
N, K = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
start_time = time.time() 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = [[] for _ in range(K+1)]
#spread until depth_th time
def spread(x, y, depth, cur):
  #if it reached the depth, return
  if cur > depth:
    return
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    #spread up, down, left, and right
    if nx >= 0 and nx < N and ny >= 0 and ny < N:
      #if it's a blank space, spread the virus
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]
        spread(nx, ny, depth, cur+1)
      #if the same virus is already there, increment the current depth and continue to spread
      elif graph[nx][nx] == graph[x][y]:
        spread(nx, ny, depth, cur+1)
      else:
        return
        
#save the location of each viruses
for i in range(N):
  for j in range(N):
    #if there's a virus
    if graph[i][j] != 0:
      #store the location of the virus
      virus[graph[i][j]].append((i, j))

for sec in range(1, S+1):
  for i in range(1, K+1):
    for x, y in virus[i]:
      spread(x, y, sec, 1)
      if graph[X-1][Y-1] != 0:
        break

print(graph[X-1][Y-1])

end_time = time.time() 
print("time :",end_time - start_time)
