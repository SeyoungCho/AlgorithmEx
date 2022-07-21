import time
N, M = map(int, input().split())
board = []
for i in range(N):
	board.append(list(map(int, input())))

start_time = time.time()
visited = [[False] * M for _ in range(N)]
def isValid(x, y):
	if x >= 0 and x < N and y >= 0 and y < M:
		return True
	return False
def dfs(x,y, visited):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	visited[x][y] = True
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if isValid(nx, ny):
			if not visited[nx][ny] and board[nx][ny] == 0:
				dfs(nx, ny, visited)
count = 0
for i in range(N):
	for j in range(M):
		if not visited[i][j] and board[i][j] == 0:
			dfs(i, j, visited)
			count += 1
print(count)
end_time = time.time()
print("time: ", end_time - start_time);