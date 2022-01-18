import time 

n, k = map(int, input().split())
start_time = time.time()

count = 0
#decrement n until it can be divided by k, repeat till n is smaller than k 
while n >= k:
  while n % k != 0:
    n -= 1
    count += 1
  n //= k
  count += 1

#decrement n till it reaches 1
while n > 1:
  n -= 1
  count += 1
print(count)
end_time = time.time()
print("time :", end_time - start_time)