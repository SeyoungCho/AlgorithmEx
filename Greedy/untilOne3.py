import time

n, k = map(int, input().split())
start_time = time.time()
count = 0

#set n to target(currently closest number that can be divided into k)
#increase count by n - target at once
#divide n by k 
#increment count
#repeat until n is smaller than k
while True:
  target = (n // k) * k
  count += (n - target)
  n = target
  if n < k:
    break
  n //= k
  count += 1

#once n is smaller than k, increase count by n - 1
count += (n - 1)
print(count)
end_time = time.time()
print("time :", end_time - start_time)