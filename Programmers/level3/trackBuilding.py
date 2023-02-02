from collections import deque

def solution(board):
    N = len(board)
    answer = []
    def bfs(init_dir, x, y, answer):
        minCost = int(1e9)
        visited = [[0 for _ in range(N)] for _ in range(N)]
        q = deque()
        q.append((init_dir, x, y, 0))
        #q.append((1, x, y, 0))
        # if board[x+1][y] == 0:
        #     q.appendleft((1, x+1, y, 100))
        #     visited[x+1][y] = 100
        # if board[x][y+1] == 0:
        #     q.appendleft((0, x, y+1, 100))
        #     visited[x][y+1] = 100
        visited[0][0] = 1
        while q:
            _dir, x, y, cost = q.popleft()
            #print(x, y, cost)
            # if x == N-1 and y == N-1:
            #     return visited[N-1][N-1]
            # if x == 0 and y == 0:
            #     if board[x+1][y] == 0:
            #         q.append((0, x+1, y, cost+100))
            #     if board[x][y+1] == 0:
            #         q.append((1, x, y+1, cost+100))
            #     continue
            # if x == 0 and y == 0:
            #     continue
            if x == N-1 and y == N-1:
                answer.append(cost)
                #continue
            if x+1 < N and board[x+1][y] == 0: #수직이동
                new_cost = cost + 600 if _dir == 0  else cost + 100
                if visited[x+1][y] == 0 or visited[x+1][y] >= new_cost:
                    q.append((1, x+1, y, new_cost))
                    visited[x+1][y] = new_cost
            if y+1 < N and board[x][y+1] == 0: #수평이동     
                new_cost = cost + 600 if _dir == 1  else cost + 100
                #print("수평이동", x, y+1, new_cost, "방향: ", _dir)
                if visited[x][y+1] == 0 or visited[x][y+1] >= new_cost:
                    q.append((0, x, y+1, new_cost))
                    visited[x][y+1] = new_cost
            if x-1 >= 0 and board[x-1][y] == 0: #수직이동   
                new_cost = cost + 600 if _dir == 0  else cost + 100
                if visited[x-1][y] == 0 or visited[x-1][y] >= new_cost:
                    q.append((1, x-1, y, new_cost))
                    visited[x-1][y] = new_cost
            if y-1 >= 0 and board[x][y-1] == 0: #수평이동 
                new_cost = cost + 600 if _dir == 1  else cost + 100
                if visited[x][y-1] == 0 or visited[x][y-1] >= new_cost:
                    q.append((0, x, y-1, new_cost))
                    visited[x][y-1] = new_cost
        #return visited[N-1][N-1]
    bfs(0, 0, 0, answer)
    bfs(1, 0, 0, answer)
    return min(answer)