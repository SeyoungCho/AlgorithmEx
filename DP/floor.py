import time

N = int(input())

start_time = time.time()
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, N+1):
  d[i] = d[i-1] + 2 * d[i-2]

print(d[N] % 796796)
end_time = time.time()
print("time :", end_time - start_time)
