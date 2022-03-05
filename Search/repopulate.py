import time
from collections import deque
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
start_time = time.time() 
move_flag = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#check the validity of coordinate
def isValidCoordinate(x, y):
	if x >=0 and x < N and y >= 0 and y < N:
		return True
	else:
		return False

#repopulate the countries that share open borders
def move_population(countries, country_num, sum):
	population = sum // country_num
	while countries:
		x, y = countries.pop()
		graph[x][y] = population

#bfs through the countries and open borders for country[x][y]
def bfs(x, y, visited):
	#if the country has already been visited, return
	if visited[x][y]:
		return
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
						if not move_flag:
							move_flag = True
	move_population(countries, country_num, sum)	
							
move_cnt = 0
while True:
	#initialize the visited array
	visited = [[False] * N for _ in range(N)]
	move_flag = False
	#bfs for all countries
	for i in range(N):
		for j in range(N):
			count, sum = 0, 0
			bfs(i, j, visited)
	if not move_flag:
		break
	else:
		move_cnt += 1

print(move_cnt)
end_time = time.time() 
print("time :",end_time - start_time)


