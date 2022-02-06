import time
N = int(input())
fear = list(map(int, input().split()))

start_time = time.time()
group_cnt = 0
fear.sort(reverse=True)
i = 0
while i < N:
  i += fear[i]
  if i > N:
    break
  else:
    group_cnt += 1
print(group_cnt)
end_time = time.time()
print("time :", end_time - start_time)