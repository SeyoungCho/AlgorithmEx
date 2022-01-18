import time

N,K = map(int, input().split())

start_time = time.time()
count = 0
#until N becomes 1, decrement it or divide it by K 
while N != 1:
  if(N % K == 0):
    N //= K
  else:
    N -= 1
  count += 1

print(count)
end_time = time.time()
print("time :", end_time - start_time)