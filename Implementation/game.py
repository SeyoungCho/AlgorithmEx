import time 

N, M = map(int, input().split())
pos = list(map(int, input().split()))
pos[0], pos[1] = pos[1], pos[0]
#pos[0]: x coordinate
#pos[1]: y coordinate
#pos[2]: direction towards which the character is facing
board = [[int(x) for x in input().split()] for y in range (N)]
start_time = time.time()

vis_cnt = 0 #visit count
rot_cnt = 0 #rotation count
visited = [[0 for col in range(M)] for row in range(N)] #is visited
visited[pos[0]][pos[1]] = 1
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#turn left
def turn_left():
  pos[2] = (pos[2] - 1) % 4

#check if the coordinate ahead is visited
def isVisited():
  x = pos[0] + steps[pos[2]][0]
  y = pos[1] + steps[pos[2]][1]
  if visited[x][y] == 1:
    return True
  else:
    return False

#check if the coordiante ahead is land
def isLand():
  x = pos[0] + steps[pos[2]][0]
  y = pos[1] + steps[pos[2]][1]
  if board[x][y] == 0:
    return True
  else:
    return False

#check if the coordinate behind is land
def isBackLand():
  direction = (pos[2] + 2) % 4
  x = pos[0] + steps[direction][0]
  y = pos[1] + steps[direction][1]
  if board[x][y] == 0:
    return True
  else:
    return False

#move forward
def forward():
  if isLand():
    if not isVisited():
      pos[0] += steps[pos[2]][0]
      pos[1] += steps[pos[2]][1]
      visited[pos[0]][pos[1]] = 1
      return True
    else:
      return False
  else:
    return False

#move backward
def backward():
  if isBackLand():
    direction = (pos[2] + 2) % 4
    pos[0] += steps[direction][0]
    pos[1] += steps[direction][1]
    return True
  else:
    return False

cnt = 0
while True:
  turn_left()
  if forward():
    continue

  turn_left()
  if forward():
    continue

  turn_left()
  if forward():
    continue

  turn_left()
  if forward():
    continue
  else:
    if backward():
      continue
    else:
      break
  
for i in visited:
  vis_cnt += i.count(1)
print(vis_cnt)
end_time = time.time()
print("time :", end_time - start_time)