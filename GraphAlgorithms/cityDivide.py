import time

N, M = map(int, input().split())
road = []
for _ in range(M):
  a, b, c = map(int, input().split())
  road.append((c,a,b))
start_time = time.time()
# use union-find data structure
parent = [i for i in range(N+1)]
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
road.sort()
max_cost = 0
result = 0
for i in road:
  cost = i[0]
  if find_parent(parent, i[1]) != find_parent(parent, i[2]):
    if max_cost < cost:
      max_cost = cost
    union_parent(parent, i[1], i[2])
    result += cost
result -= max_cost
print(result)
end_time = time.time()
print("time :", end_time - start_time)