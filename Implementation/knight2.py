import time 

pos = list(input())

start_time = time.time()
count = 0
x = int(ord(pos[0]) - int(ord('a'))) + 1
y = int(pos[1])
#make a list of all possible moves
steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
  next_x = x + step[0]
  next_y = y + step[1]
  if next_x >= 1 and next_x <=8 and next_y >= 1 and next_y <=8:
    count += 1

end_time = time.time()
print(count)
print("time :", end_time - start_time)