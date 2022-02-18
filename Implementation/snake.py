import time
from collections import deque
N = int(input())  #board size
K = int(input())  #number of apples
#play board
board = [[0 for _ in range(N+2)] for _ in range(N+2)]
for _ in range(K):
  i, j = map(int, input().split())
  #place the apples
  board[i][j] = 2
dirChange = [0] * (N * N) 
L = int(input())  #number of changes in directions
#dirChange[i] holds to which direction the snake is heading at ith sec
for _ in range(L):
  t, D = input().split()
  dirChange[int(t)] = 1 if D == 'D' else -1

start_time = time.time() 
#snake : 1
#wall : -1
#apple : 2
#vacant space : 0

#board initialization 
board[0] = [-1] * (N+2)
board[N+1] = [-1] * (N+2)
for i in range(1, N+1):
  board[i][0], board[i][N+1] = -1, -1

#direction list
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#place the snake 
board[1][1] = 1
#snake list
snake = deque()
s = 1
head = (1, 1) #initial location of head
snake.appendleft(head)
_dir = 0 #initial direction
while True:
  #current head
  hx, hy = snake[0][0], snake[0][1]
  #coordinate ahead
  ax, ay = hx + direction[_dir][0], hy + direction[_dir][1]
  #wall or body ahead
  if board[ax][ay] == -1 or board[ax][ay] == 1:
    break
  #apple ahead
  elif board[ax][ay] == 2:
    #move the head forward
    snake.appendleft((ax, ay))
    board[ax][ay] = 1
  #nothing ahead
  else:
    #move the head forward
    snake.appendleft((ax, ay))
    board[ax][ay] = 1
    #remove the tail 
    prev_tail = snake.pop() 
    board[prev_tail[0]][prev_tail[1]] = 0
  #remain or change the direction
  _dir = (_dir + dirChange[s]) % 4
  s += 1

print(s)
end_time = time.time() 
print("time :",end_time - start_time)
