#radix sort solution
import time
N = int(input())
parts = [0] * 1000001
for i in input().split():
  parts[int(i)] = 1
M = int(input())
order = list(map(int, input().split()))
start_time = time.time()

for i in order:
  if parts[i] == 1:
    print("yes", end=" ")
  else:
    print("no", end=" ")
print()
end_time = time.time() 
print("time :", end_time - start_time)
