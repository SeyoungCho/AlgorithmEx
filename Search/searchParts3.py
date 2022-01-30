#set solution
import time
N = int(input())
parts = set(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))
start_time = time.time()
for i in order:
  if i in parts:
    print("yes", end=" ")
  else:
    print("no", end=" ")
print()
end_time = time.time() 
print("time :", end_time - start_time)
