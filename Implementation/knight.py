import time 

pos = list(input())

start_time = time.time()
count = 0
#convert coordinates into numbers
x = ord(pos[0])
y = int(pos[1])
row = [97, 98, 99, 100, 101, 102, 103, 104]
col = [1,2,3,4,5,6,7,8]
#validate all the possible cases
if x - 1 in row and y - 2 in col:
  count += 1
if x + 1 in row and y - 2 in col:
  count += 1
if x + 2 in row and y - 1 in col:
  count += 1
if x + 2 in row and y + 1 in col:
  count+= 1
if x + 1 in row and y + 2 in col:
  count+= 1
if x - 1 in row and y + 2 in col:
  count += 1
if x - 2 in row and y + 1 in col:
  count += 1
if x - 2 in row and y - 1 in col:
  count += 1
end_time = time.time()
print(count)
print("time :", end_time - start_time)