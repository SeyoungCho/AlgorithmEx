import time

N = int(input())

start_time = time.time()
#just count all the possible time(완전탐색))
count = 0
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

end_time = time.time()
print(count)
print("time :", end_time - start_time)