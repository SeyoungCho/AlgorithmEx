import time

N = int(input())
arr = list(map(int, input().split()))
start_time = time.time()
d = [0] * (N+1)

d[1] = arr[0]
for i in range(2, N+1):
  d[i] = max(d[i-1], d[i-2]+arr[i-1])

print(d[N])
end_time = time.time()
print("time :", end_time - start_time)