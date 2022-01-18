import time

N = map(int, input())
route = input().split()
start_time = time.time()

#start coordinate
x, y = 1, 1

#increment/decrement x or y according to the directions
for dir in route:
  if dir == 'L':
    if y != 1:
      y -= 1
  elif dir == 'R':
    if y != N:
      y += 1
  elif dir == 'U':
    if x != 1:
      x -= 1
  elif dir == 'D':
    if x != N:
      x += 1
end_time = time.time()
print(x, y)
print("time :", end_time - start_time)