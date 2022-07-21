import sys
from collections import deque
N, L, R = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#check the validity of coordinate
def isValidCoordinate(x, y):
	if x >=0 and x < N and y >= 0 and y < N:
		return True
	else:
		return False


#bfs through the countries and open borders for country[x][y]
def bfs(x, y):
	global move_flag
	queue = deque([(x,y)])
	countries = [(x, y)]
	sum = graph[x][y]
	visited[x][y] = True
	country_num = 1
	while queue:
		a, b = queue.popleft()
		for i in range(4):
			nx,ny = a+dx[i], b+dy[i]
			if isValidCoordinate(nx, ny):
				diff = abs(graph[a][b]-graph[nx][ny])
				if diff >= L and diff <= R:
					if not visited[nx][ny]:
						visited[nx][ny] = True
						queue.append((nx, ny))
						countries.append((nx,ny))
						sum += graph[nx][ny]
						country_num += 1
	if len(countries) > 1:
		move_flag = True
	for i, j in countries:
		graph[i][j] = sum // country_num
							
move_cnt = 0
while True:
	#initialize the visited array
	visited = [[False] * N for _ in range(N)]
	move_flag = False
	#bfs for all countries
	for i in range(N):
		for j in range(N):
			if not visited[i][j]:
				bfs(i, j)
	if not move_flag:
		break
	move_cnt += 1

print(move_cnt)

