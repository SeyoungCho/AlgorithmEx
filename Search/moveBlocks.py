import time
from collections import deque

start_time = time.time()

# up, down, left, right move
move = [(-1, 0, -1, 0), (1, 0, 1, 0), (0, -1, 0, -1), (0, 1, 0, 1)]
#rotation rot[0] : horizontal, rot[1]: vertical
rot = [[(-1, 0, 0, 1), (0, 0, 1, -1), (-1, 1, 0, 0), (0, 1, 1, 0)],
       [(0, -1, -1, 0), (0, 0, -1, 1), (1, -1, 0, 0), (1, 0, 0, 1)]]
#obstacle check points
cp = [[(-1, 1), (1, 1), (-1, -1), (1, -1)], [(1, -1), (1, 1), (-1, -1),
                                             (-1, 1)]]


#checks if the next location is valid
def isValid(x1, y1, x2, y2, n):
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n or x2 < 0 or x2 >= n or y2 < 0 or y2 >= n:
        return False
    return True


#checks if the next location is empty
def isEmpty(x1, y1, x2, y2, board):
    if board[x1][y1] == 0 and board[x2][y2] == 0:
        return True
    return False


#checks if current form is horizontal
def checkType(x1, y1, x2, y2):
    if x1 == x2:
        return 0
    return 1


#checks if the block arrived at the end
def isEnd(x1, y1, x2, y2, n):
    if (n - 1, n - 1) in [(x1, y1), (x2, y2)]:
        return True
    return False


#checks if there is no obstacle when rotating
def isRotatable(x1, y1, x2, y2, type, rot_num, board):
    if rot_num == 0 or rot_num == 1:
        x, y = x1, y1
    else:
        x, y = x2, y2
    cx, cy = tuple(sum(elem) for elem in zip((x, y), cp[type][rot_num]))
    #print(x, y, cx, cy, type, rot_num)
    if board[cx][cy] == 0:
        return True
    else:
        return False

def solution(board):
    answer = 0
    n = len(board[0])
    #visited[][][0]: Left
    #visited[][][1]: Up
    visited = [[[False] * n for _ in range(n)] for _ in range(4)]
    visited[0][0][0] = True
    queue = deque([(0, 0, 0, 1, 0)])
    while queue:
        x1, y1, x2, y2, t = queue.popleft()
        #print("\npopped from the queue", x1, y1, x2, y2)
        #check if the block arrived at the end
        if isEnd(x1, y1, x2, y2, n):
            answer = t
            break
        #try moving
        type = checkType(x1, y1, x2, y2)
        for i in range(4):
            _x1, _y1, _x2, _y2 = tuple(
                sum(elem) for elem in zip(move[i], (x1, y1, x2, y2)))
            if isValid(_x1, _y1, _x2, _y2, n):
                if isEmpty(_x1, _y1, _x2, _y2,
                           board) and not visited[type][_x1][_y1]:
                    visited[type][_x1][_y1] = True
                    queue.append((_x1, _y1, _x2, _y2,t + 1))  #enqueue the next location and time
        #try rotating
        for i in range(4):
            _x1, _y1, _x2, _y2 = tuple(
                sum(elem) for elem in zip(rot[type][i], (x1, y1, x2, y2)))
            new_type = checkType(_x1, _y1, _x2, _y2)
            if isValid(_x1, _y1, _x2, _y2, n):
                if isEmpty(_x1, _y1, _x2, _y2, board) and not visited[new_type][_x1][_y1] and isRotatable(x1, y1, x2, y2, type, i, board):
                    visited[new_type][_x1][_y1] = True
                    queue.append((_x1, _y1, _x2, _y2, t + 1))  #enqueue the next location and time
    return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1],[1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
end_time = time.time()
print("time :", end_time - start_time)