import time

N, K = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
start_time = time.time()
#sort a in ascending order
a_list.sort()
#sort b in descending order
b_list.sort(reverse=True)
#swap each elements starting from the first indexes
for i in range(K):
  if a_list[i] < b_list[i]:
    a_list[i], b_list[i] = b_list[i], a_list[i]
  else:
    break
print(sum(a_list))
end_time = time.time()
print("time :", end_time - start_time)