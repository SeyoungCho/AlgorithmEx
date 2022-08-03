import time
import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N+1)
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
start_time = time.time()


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)
cnt = 0
max = 0
for i in range(1, len(distance)):
    if distance[i] == INF:
        continue
    else:
        cnt += 1
        if max < distance[i]:
            max = distance[i]

print(cnt-1, max)

end_time = time.time()
print("time: ", end_time - start_time)
