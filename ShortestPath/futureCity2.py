import time
INF = int(1e9) # Infinity
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)] # 2차원 리스트 초기화

#자기 자신으로의 경로는 0으로 초기화
for i in range(1, N+1):
	graph[i][i] = 0

#M개의 줄 입력받기
for _ in range(M):
	a, b = map(int, input().split());
	graph[a][b] = 1
	graph[b][a] = 1

#K와 X 입력받기
X, K = map(int, input().split())
start_time = time.time()

for i in range(1, N+1):
	for j in range(1, N+1):
		for k in range(1, N+1):
			graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

dist = graph[1][K] + graph[K][X]

if dist >= INF:
	print("-1")
else:
	print(dist)
	
end_time = time.time()
print("time :",end_time-start_time)