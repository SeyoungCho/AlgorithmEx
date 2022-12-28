def isAvailable(x, y, graph):
    if x >= 0 and x <= 4 and y >= 0 and y <= 4 and graph[x][y] != 'X':
        return True
    else:
        return False    
    
# graph[i][j] 에서 거리 2 이내의 P가 있으면 True, 없으면 False
def find_p(graph, x, y, dist, visited):
    visited.append((x,y))
    if graph[x][y] == 'P':
        if dist > 0:
            return True
    if dist == 2:
        return False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for row, col in zip(dx, dy):
        if (x+row, y+col) not in visited:
            if isAvailable(x+row, y+col, graph): # 범위 안에 있고 X가 아닌 경우
                if find_p(graph, x+row, y+col, dist+1, visited):
                    return True
    return False
        
def solution(places):
    answer = []
    for idx, graph in enumerate(places):
        flag = True
        for i in range(len(graph)):
            if not flag:
                break
            for j in range(len(graph)):
                if graph[i][j] == 'P':
                    visited = []
                    if find_p(graph, i, j, 0, visited):
                        flag = False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)      
    return answer