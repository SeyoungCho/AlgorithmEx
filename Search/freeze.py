import time

N,M = map(int, input().split())
tray = [[int(x) for x in input().split()] for y in range(N)]
count = 0
start_time = time.time()
def dfs(x,y):
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  #if you haven't visited current node
  if tray[x][y] == 0:
    tray[x][y] = 1
    #check up, down, left, right of the current node
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

for i in range(N):
  for j in range(M):
    if dfs(i, j) == True:
      count += 1

print(count)

end_time = time.time()
print("time :", end_time - start_time)