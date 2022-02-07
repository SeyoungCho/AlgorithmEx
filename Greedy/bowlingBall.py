import time
N, M = map(int, input().split())
balls = list(map(int, input().split()))
start_time = time.time()

result = 0
#check all the possible cases with double for loop
for i in range(N):
  for j in range(i+1, N):
    if balls[i] != balls[j]:
      result += 1

print(result)


end_time = time.time()
print("time :", end_time - start_time)