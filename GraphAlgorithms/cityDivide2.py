import time

N, M = map(int, input().split())
edges = []

for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

start_time = time.time()

cost_sum = 0
max_cost = 0
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i


def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    else:
        return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        cost_sum += cost
        max_cost = cost
        union_parent(parent, a, b)

answer = cost_sum - max_cost
print(answer)
end_time = time.time()
print("time: ", end_time - start_time)
