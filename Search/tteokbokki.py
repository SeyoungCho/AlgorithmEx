#Sequential Search solution
import time
N, M = map(int, input().split())
tteoks = list(map(int, input().split()))

start_time = time.time()

tteoks.sort(reverse=True)
#h is height of the cutter, initialize it to the tallest of the tteoks
h = tteoks[0]

output = [0.00001]
while True:
  output = [i - h for i in tteoks if i > h]
  if sum(output) >= M:
    break
  h -= 1
print(h)

end_time = time.time() 
print("time :", end_time - start_time)