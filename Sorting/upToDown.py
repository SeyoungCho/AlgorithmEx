import time

N = int(input())
arr = []
for i in range(N):
  arr.append(int(input()))


start_time = time.time()
result = reversed(sorted(arr))
for i in result:
  print(i, end=" ")
print()
end_time = time.time() 
print("time :", end_time - start_time)