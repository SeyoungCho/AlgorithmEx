import time
N = int(input())
coin = list(map(int, input().split()))
start_time = time.time()

coin.sort()
#if the smallest unit is larger than 1, the answer is 1
result = 1
if coin[0] == 1:
  i = 0
  while True:
    if coin[i+1] > result + 1:
      result += 1
      break
    else:
      result += coin[i+1]
    i += 1
 
print(result)

end_time = time.time()
print("time :", end_time - start_time)