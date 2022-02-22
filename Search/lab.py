import time
from itertools import combinations

N, M = map(int, input().split())
graph = [[int(x) for x in input().split()] for y in range(N)]
      
start_time = time.time() 
count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maxSpace = N*M

#dfs from the current coordinate and spread the virus into spaces
def spread(x, y, visited):
  global count
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    #spread up, down, left, and right
    if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == False and graph[nx][ny] == 0:
      visited[nx][ny] = True
      count += 1
      spread(nx, ny, visited)
  
#make a list of indices of each structure
wallCnt = 0
virus = []
space = []
maxSpace = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      space.append((i,j))
    elif graph[i][j] == 1:
      wallCnt += 1
    else:
      virus.append((i,j))

#check every possible cases where new walls are built
for case in combinations(space, 3):
  visited = [[False for _ in range(M)] for _ in range(N)]
  #build new walls
  for nw in case:
    x, y = nw[0], nw[1]
    graph[x][y] = 1
  #spread the virus
  for v in virus:
    x, y = v[0], v[1]
    spread(x, y, visited)
  #remove the walls
  for nw in case:
    x, y = nw[0], nw[1]
    graph[x][y] = 0
  space = (N*M) - (wallCnt + 3 + len(virus) + count)
  maxSpace = max(maxSpace, space)
  count = 0

print(maxSpace)
  
end_time = time.time() 
print("time :",end_time - start_time)