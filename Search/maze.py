import time
from collections import deque
N,M = map(int, input().split())
maze = []
for i in range(N):
  maze.append(list(map(int, input())))
start_time = time.time()

def bfs(x, y):
  queue = deque([[x,y]])
  while queue:
    a, b = queue.popleft()
    #check up, down, left, right of the current node
    if a > 0 and maze[a-1][b] == 1:
      queue.append([a-1, b])
      maze[a-1][b] = maze[a][b] + 1
    if a < N-1 and maze[a+1][b] == 1:
      queue.append([a+1, b])
      maze[a+1][b] = maze[a][b] + 1
    if b > 0 and maze[a][b-1] == 1:
      queue.append([a, b-1])
      maze[a][b-1] = maze[a][b] + 1
    if b < M-1 and maze[a][b+1] == 1:
      queue.append([a, b+1])
      maze[a][b+1] = maze[a][b] + 1

bfs(0,0)
print(maze[N-1][M-1])
  
end_time = time.time()
print("time :", end_time - start_time)